from django.db import models

# Create your models here.
class Pokemon (models.Model):
    
    
    
    
    class PokemonType(models.TextChoices):
        WATER = 'WA', ('WATER')
        GRASS = 'GR',('GRASS')
        GHOST = 'GH',('GHOST')
        STEEL = 'ST',('STEEL')
        FAIRY = 'FA',('FAIRY')
    
    name=models.CharField(max_length=30)
    type= models.CharField(choices=PokemonType.choices,max_length=30)
    hp=models.PositiveIntegerField()
    active=models.BooleanField(default=True)
    name_fr=models.CharField(max_length=30, default="")
    name_ar=models.CharField(max_length=30, default="")
    name_jp=models.CharField(max_length=30, default="")
    created_at=models.DateTimeField(auto_created=True)
    modified_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name