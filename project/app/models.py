from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NameForm(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return str(self.name)
    
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    division = models.CharField( max_length=50)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=50)
    villorroad = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    Mobile_number = models.IntegerField()
    image = models.ImageField( default='image.png',null=True , blank=True)
    
    
    def __str__(self):
        return str(self.name)
    
    
from django.db import models


ch = (
    ('Pending','Pending'),
    ('approved','approved'),
    
)

class YoutubeChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=255)
    statue = models.CharField(max_length=255 ,default='Pending', choices=ch)
    channel_url = models.URLField()
    channel_id = models.CharField(max_length=255 , unique=True)
    description = models.TextField()

    def __str__(self):
        return self.channel_name

class AddMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    earning = models.IntegerField( )
    payment = models.IntegerField( )
    
from django.conf import settings
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')
   

    def __str__(self):
        return "Site Settings"

class EmailSettings(models.Model):
    host_user = models.EmailField()
    host_password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        settings.EMAIL_HOST_USER = self.host_user
        settings.EMAIL_HOST_PASSWORD = self.host_password
        super().save(*args, **kwargs)
        
    