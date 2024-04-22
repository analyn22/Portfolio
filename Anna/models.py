from django.db import models

class Personal(models.Model):
    Profile = models.ImageField(upload_to="Profile", height_field=None, width_field=None, max_length=None)
    Tag = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    description = models.TextField()
    footer = models.TextField()

    class Meta:
        verbose_name = ("Personal")
        verbose_name_plural = ("Personal Details")

    def __str__(self):
        return self.Name


class Social(models.Model):
    ICON_CHOICES = (
    ('facebook','facebook'),
    ('gitlab','Git Lab'),
    ('github','Git Hub'),
    ('messenger','Messenger'),
    ('twitter','Twitter'),
    ('google','Google'),
    ('linkedin','LinkedIn'),
    ('youtube','Youtube'),
    ('instagram','Instagram'),
    ('pinterest','Pinterest'),
    ('snapchat-ghost','Snapchat Ghost'),
    ('skype','Skype'),
    ('android','Andriod'),
    ('dribbble','Dribble'),
    ('vimeo','Vimeo'),
    ('tumblr','Tumblr'),
    ('vine','Vine'),
    ('foursquare','Foursquare'),
    ('stumbleupon','Stumbleupon'),
    ('flickr','Flickr'),
    ('yahoo','Yahoo'),
    ('soundcloud','Soundcloud'),
    ('reddit','Reddit'),
    ('rss','Rss'),

)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    link = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Social")
        verbose_name_plural = ("Socials")

    def __str__(self):
        return self.link

    
