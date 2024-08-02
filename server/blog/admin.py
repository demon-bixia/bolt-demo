from django_api_admin.sites import site
from .models import Author, Book

# Register your models here.

site.register(Author)
site.register(Book)
