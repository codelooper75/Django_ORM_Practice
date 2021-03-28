from django.contrib import admin
from .models import Blog, Author, Entry, Editor

# admin.site.register(Author)
# admin.site.register(Entry)
# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',"tagline",'id', 'editor') #колонки которые будут видны в админке
    list_display_links = ("name",)
    search_fields = ('name','tagline') #обязательно указывать по какому полю в creator ищем

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("headline", 'blog','id', 'body_text','pub_date','rating' ) #колонки которые будут видны в админке
    list_display_links = ("headline",)
    search_fields = ('blog',"headline", 'body_text',) #обязательно указывать по какому полю в creator ищем
    list_filter = ("blog",'authors')

@admin.register(Author)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name',"email",'id',) #колонки которые будут видны в админке
    list_display_links = ("name",)
    search_fields = ('name',"email",) #обязательно указывать по какому полю в creator ищем

@admin.register(Editor)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name',"email",'id') #колонки которые будут видны в админке
    list_display_links = ("name",)
    search_fields = ('name',"email",) #обязательно указывать по какому полю в creator ищем