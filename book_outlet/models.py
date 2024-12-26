from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=30, null=True)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", db_index=True, blank=True)

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    # def save(self, *args, **kwargs):
    #     title_words = self.title.split(" ")
    #     lim_title = (
    #         " ".join(title_words[:9]) if len(title_words) > 1 else title_words[0]
    #     )
    #     self.slug = slugify(lim_title)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
