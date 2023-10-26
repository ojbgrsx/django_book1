from django.db import models


# Create your models here.

class Book(models.Model):
    ACTUALITY = (
        ('Actual', 'Actual'),
        ('50/50', '50/50'),
        ('Not actual', 'Not actual'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    actuality = models.CharField(max_length=100, choices=ACTUALITY, default=ACTUALITY[0], null=True)
    video = models.URLField(null=True)
    cost = models.SmallIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )
    title_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
       return f"Review for {self.title_book}"