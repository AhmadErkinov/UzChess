from django.db import models

# Create your models here.


class TopCourses(models.Model):


    course_title = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    course_all_button = models.URLField()

class TopBooks(models.Model):
    
    book_title = models.ForeignKey("library.Library", on_delete=models.CASCADE)
    book_watching = models.IntegerField()
    book_all_button = models.URLField()


class News(models.Model):
    
    title = models.ForeignKey("news.News", on_delete=models.CASCADE)

class DayGame(models.Model):

    game_type = models.FileField(upload_to="main/")

    player_f_name = models.CharField(max_length=255)
    player_f_status = models.CharField(max_length=255)

    player_s_name = models.CharField(max_length=255)
    player_s_status = models.CharField(max_length=255)

    watch_button = models.URLField(max_length=255)

class Main(models.Model):
    
    topcourses = models.ForeignKey(TopCourses, on_delete=models.CASCADE)
    topbooks = models.ForeignKey(TopBooks, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    daygame = models.ForeignKey(DayGame, on_delete=models.CASCADE)

    main = models.URLField(max_length=255)
    news_page = models.URLField(max_length=255)
    courses = models.URLField(max_length=255)
    library = models.URLField(max_length=255)

    search = models.URLField(max_length=255)
    basket = models.URLField(max_length=255)
    bell = models.URLField(max_length=255)

    login = models.URLField(max_length=255)

