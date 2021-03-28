from django.contrib import admin
from .models import Book, Author, Library


@admin.register(Library)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id',"name", 'address') #колонки которые будут видны в админке
    list_display_links = ("name",)
    search_fields = ('name',"address",) #обязательно указывать по какому полю в creator ищем
    # list_filter = ("genre",)



@admin.register(Author)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id','name',"email",'born') #колонки которые будут видны в админке
    list_display_links = ("name",)
    search_fields = ('name',"email",'born') #обязательно указывать по какому полю в creator ищем


@admin.register(Book)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id',"title", 'genre','pub_date','length') #колонки которые будут видны в админке
    list_display_links = ("title",)
    search_fields = ('title',"genre",) #обязательно указывать по какому полю в creator ищем
    list_filter = ("genre",)

