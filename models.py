from django.db import models

# Create your models here.
class defi(models.Model):
    title = models.CharField(max_length=200)

    mr = models.CharField(max_length=400)
    fr = models.CharField(max_length=400)
    en = models.CharField(max_length=400)
    sp = models.CharField(max_length=400)

    face = models.CharField(max_length=400)
    twit = models.CharField(max_length=400)

    son = models.FileField(blank=True, null=True)
    hasAudio = models.BooleanField(default=False)

    def __str__(self):
        return self.title

'''
name | link | type | rating
'''
class bookMark(models.Model):
    diff = (
	    ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
         )

    title = models.CharField(max_length=100)
    link = models.CharField(max_length=400)
    cate = models.ForeignKey('catego' )
    rate = models.CharField(max_length=20 , choices=diff)

    def __str__(self):
        return self.title

#########################
#sub catego
#########################
class catego(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

