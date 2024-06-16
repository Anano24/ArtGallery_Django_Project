from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'category'


    def __str__(self):
        return self.name



class GalleryItems(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='gallery_items_img/', null=True, blank=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'galleryitems'

