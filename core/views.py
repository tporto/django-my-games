from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Game, Image
from .forms import GameForm, ImageForm

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
    print(form)
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
    #if request.method == 'POST':
    form = GameForm(request.POST or None,request.FILES or None,initial={'game_type': '1'})
    #else:
     #   form = GameForm()
    return save_game_form(request, form, 'games/includes/partial_game_create.html')

def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
    else:
        form = GameForm(instance=game)
    return save_game_form(request, form, 'games/includes/partial_game_update.html')

def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    data = dict()
    if request.method == 'POST':
        game.delete()
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

def create_image(request):
    form = ImageForm(request.Post or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect()
