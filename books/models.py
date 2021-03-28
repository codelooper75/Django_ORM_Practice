from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} on {self.address}"

class Author(models.Model):
    name = models.CharField(max_length=200)
    born = models.DateField(blank=True, null=True)
    email = models.EmailField()
    #books id

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.TextField(blank=True, null=True)
    pub_date = models.DateField()
    length = models.IntegerField()
    authors = models.ManyToManyField(Author)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"



# class Editor(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#     editor = models.ForeignKey(Editor, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return self.name
#
#
