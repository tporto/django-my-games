from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='images/')
    cover = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Game(models.Model):
    PS4 = 1
    XONE = 2
    PC = 3
    WII = 4
    MOBILE = 5
    GAME_TYPES = ((PS4,'PS4'),(XONE,'Xbox One'),(PC,'PC'),(WII,'Wii U'),(MOBILE,'Mobile'),)
    title = models.CharField(max_length=155)
    publication_date = models.DateField(null=True)
    developer = models.CharField(max_length=155,null=True,blank=True)
    image = models.ForeignKey(Photo)
    game_type = models.PositiveSmallIntegerField(choices=GAME_TYPES)