from django.db import models
from django.contrib.auth.models import User

# That IS Models For User Profile.

# That IS For Personal User Profile
class Per_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=15, null=True)

    city = models.TextField(max_length=50, null=True)
    pin = models.TextField(max_length=6, null=True)
    contry = models.TextField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    wmobile = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True)
    married = models.CharField(max_length=10, null=True)
    occupation = models.CharField(max_length=50, null=True)

    profile = models.ImageField(upload_to='profile', blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        verbose_name = "Person Detail"
        verbose_name_plural = "Person Details"


# That IS For Bussiness User Profile
class Bus_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=15, null=True)

    gst = models.CharField(max_length=50, null=True)
    tag = models.CharField(max_length=6, null=True)
    dis = models.TextField(max_length=50, null=True)
    category = models.TextField(max_length=254, null=True)
    add = models.TextField(max_length=10, null=True)
    city = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=10, null=True)
    pin = models.CharField(max_length=50, null=True)

    logo = models.ImageField(upload_to='logo', blank=True)
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Business Detail"
        verbose_name_plural = "Business Details"


