from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Library, self).save(args, kwargs)
    
class LibraryForm(ModelForm):
    class Meta:
        model = Library
        #fields = '__all__'
