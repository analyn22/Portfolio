from django.db import models
from django.utils.text import slugify

class Projects(models.Model):

    Image = models.ImageField(upload_to="Projects", height_field=None, width_field=None, max_length=None)
    Title = models.CharField( max_length=100)
    Description = models.TextField()
    date_added = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)


    class Meta:
        verbose_name = ("Projects")
        verbose_name_plural = ("My Projects")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Title.replace(' ', '-'))
        super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title


class Design(models.Model):

    name = models.CharField(max_length=50)
    percentage = models.IntegerField()

    class Meta:
        verbose_name = ("Design")
        verbose_name_plural = ("Designing")

    def __str__(self):
        return self.name
    
class Developing(models.Model):

    name = models.CharField(max_length=50)
    percentage = models.IntegerField()


    class Meta:
        verbose_name = ("Developing")
        verbose_name_plural = ("Developing")

    def __str__(self):
        return self.name
    

class External(models.Model):

    context = models.CharField(max_length=50)
    details = models.CharField(max_length=150)

    class Meta:
        verbose_name = ("External")
        verbose_name_plural = ("External Details")

    def __str__(self):
        return self.context


class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField()
    date_send = models.DateField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

    


  