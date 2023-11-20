from django.db import models

# Create your models here.


class News(models.Model):
    
    title = models.CharField(max_length=255)
    discription = models.TextField()
    
    posted_date = models.DateTimeField()

    post_url = models.URLField(max_length=255)

    image = models.FileField(upload_to='news', blank=True)

    if __name__ =="__main__":
        search_field = ['title', 'body']
    