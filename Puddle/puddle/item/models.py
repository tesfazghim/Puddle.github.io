# import user 
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Category of items, so distinction between toys or furnitures
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        #orders the names of the categories in asc order, include comma to make it iterable
        ordering = ('name', )
        '''have appropriate plural name for the category, django by defauly adds 's' 
            so it was Categorys, and we fixed it using the line below'''
        verbose_name_plural = "Categories"
    
    # show the name of the category ex. instead of showing Category(1) we use the following to show 'Toys'
    def __str__(self):
        return self.name
 
# actual items are defined in this class  
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image=models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # user to be imported from db
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name