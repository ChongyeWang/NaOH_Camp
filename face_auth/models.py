from django.db import models

class FaceAuth(models.Model): 
  
    name = models.CharField(max_length=30)
    
    image = models.ImageField(upload_to ='face/') 
