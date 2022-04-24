from email import message
from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    Gender = models.CharField(max_length=2,default='')
    SSC = models.CharField(max_length=3,default='')
    HSC = models.CharField(max_length=3,default='')
    Phy = models.CharField(max_length=3,default='')
    Chem = models.CharField(max_length=3,default='')
    Bio = models.CharField(max_length=3,default='')
    Maths = models.CharField(max_length=3,default='')
    NatureWork = models.CharField(max_length=2,default='')
    Literacy = models.CharField(max_length=2,default='')
    Living = models.CharField(max_length=2,default='')
    Finance = models.CharField(max_length=3,default='')
    hrs = models.CharField(max_length=2,default='')
    CreativeThink = models.CharField(max_length=2,default='')
    SelfLearn = models.CharField(max_length=2,default='')
    Coding =models.CharField(max_length=2,default='')
    Pubskill = models.CharField(max_length=2,default='')
    ReadWrite = models.CharField(max_length=2,default='')
    Comp = models.CharField(max_length=3,default='')
    Extracurr = models.CharField(max_length=3,default='')
    Teams = models.CharField(max_length=3,default='')
    Sports = models.CharField(max_length=3,default='')
    ReadWrite =models.CharField(max_length=3,default='')
    Subject = models.CharField(max_length=3,default='')
    HWSW = models.CharField(max_length=3,default='')
    gap = models.CharField(max_length=3,default='')
    id=models.CharField(primary_key=True,max_length=100, blank=True, unique=True, default=uuid.uuid4)
    def __unicode__(self):
        return self.id
    

class User(models.Model):
    name=models.CharField(max_length=30,default='')
    email=models.EmailField(max_length=20,default='')
    phoneno=models.CharField(max_length=12,default='')

    def __str__(self) -> str:
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=30,default="")
    email=models.EmailField(max_length=30,default="")
    message=models.CharField(max_length=50,default="")

    def __str__(self) -> str:
        return self.name