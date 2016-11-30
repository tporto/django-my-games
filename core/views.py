from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Game, Photo, GamePhoto
from .forms import GameForm, PhotoForm

# Create your views here.
def paginacao(request):
    lista = Game.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(lista,2)
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(paginator.num_pages)
    return games

def game_list(request):
    return render(request,'games/list.html',{'games': paginacao(request)})

def save_game_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_game_list'] = render_to_string('games/includes/partial_game_list.html', {
                'games': paginacao(request)
            })
            data['message'] = 'Saved successfully'
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request)
    return JsonResponse(data)

def game_create(request):
    form = GameForm(request.POST or None,initial={'game_type': '1'})
    return save_game_form(request, form, 'games/includes/partial_game_create.html')

def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
    else:
        form = GameForm(instance=game)
    return save_game_form(request, form, 'games/includes/partial_game_update.html')

def game_show(request,pk):
    game = get_object_or_404(Game, pk=pk)
    photos = GamePhoto.objects.filter(game_id=pk)
    return render(request,'games/show.html',{'g': game, 'photos': photos})

def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    data = dict()
    if request.method == 'POST':
        photos = GamePhoto.objects.filter(game_id=pk)
        if photos is not None:
            for p in photos:
                Photo.objects.get(id=p.photo_id).delete() #deletar da tabela photo
            photos.delete() #deletar o album
        game.delete() #deletar game
        data['form_is_valid'] = True
        data['message'] = 'Removed successfully'
        data['html_game_list'] = render_to_string('games/includes/partial_game_list.html', {
            'games': paginacao(request)
        })
    else:
        context = {'game': game}
        data['html_form'] = render_to_string('games/includes/partial_game_delete.html',
            context,
            request,
        )
    return JsonResponse(data)

def image_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    data = dict()
    if request.method == 'POST':
        photo.delete()
        data['form_is_valid'] = True
        data['message'] = 'Removed successfully'
    else:
        context = {'photo': photo}
        data['html_form'] = render_to_string('images/delete_image.html',context,request,)
    return JsonResponse(data)

def image_show(request,pk):
    photo = get_object_or_404(Photo, pk=pk)
    data = dict()
    if photo is None:
        data['form_is_valid'] = False
    else:
        data['form_is_valid'] = True
        data['html_form'] = render_to_string('images/show_image.html',{'p': photo}, request, )
    return JsonResponse(data)

def create_image(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.cover = True
        photo.save()
        messages.success(request,'Saved successfully')
        return redirect('image_list')
    return render(request,'images/create_image.html',{'form': form})

def image_list(request):
    lista = Photo.objects.all()
    return render(request,'images/list_image.html',{'images': lista})

class UploadView(View):
    def post(self,request, pk):
        form = PhotoForm(self.request.POST, self.request.FILES)
        form.data['title'] = 'A' #faço isso para o form passar
        print(form)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.title = photo.file.name
            photo.save()
            #save gallery
            relation = GamePhoto()
            relation.photo_id = photo.id
            relation.game_id = pk
            relation.save()

            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)