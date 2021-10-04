from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=100,verbose_name="Ad")
    last_name = models.CharField(max_length=100,verbose_name="Soyad")
    designation = models.CharField(max_length=255,verbose_name="Təyinat")
    photo = models.ImageField(upload_to = 'photos/teams')
    facebook_link = models.CharField(max_length=500,verbose_name="Facebook")
    instagram_link = models.CharField(max_length=500,verbose_name="Instagram")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Komanda Heyyəti"
        verbose_name_plural = "Komanda Üzvləri"