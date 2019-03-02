# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

#All lines starting with from or import are lines that add some bits from other files
#class is a special keyword that indicates that we are defining an object.
#Post is the name of our model
#models.Model means that the Post is a Django Model.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title