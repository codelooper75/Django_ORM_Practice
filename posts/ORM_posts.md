#imports 
from posts.models import Author, Editor, Blog, Entry




class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Editor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, null=True)


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    rating = models.IntegerField()


####################################
########## Many-to-one ( ForeignKey) #########
####################################
#https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/
Entry (many) to Blog (one) relationship
e1 = Entry.objects.get(pk=1)  #retrive one                  <Entry: PUMP NOK>
e1.blog                       #show forign key relation     <Blog: Wall Street Bets>
e1.blog.name                  #show field of for key relation   'Wall Street Bets'
e1.blog.editor.name           #going even deeper                   'Broke Dude'

b1 = Blog.objects.get(pk=1)
b1.entry_set.all()             #show all entries of blog     <QuerySet [<Entry: PUMP NOK>, <Entry: How not to get poor>, <Entry: PUMP EMC>]>











#Createing new
new_blog = Blog(name='Food blog', tagline='This is the best food blog')
new_blog.save()


#retreving
all_blogs = Blog.objects.all()
all_blogs[0] #will get you first blog from queryset (classic Python slicing)

Blog.objects.filter(name='Food blog') #<QuerySet [<Blog: Food blog>]>
Blog.objects.filter(name__startswith='Food') #<QuerySet [<Blog: Food blog>]>
Blog.objects.filter(name__endswith='blog') #<QuerySet [<Blog: Food blog>]>
#note "i" means case insensetive match
Blog.objects.filter(name__iexact='Food bloG') #case incensetive match (as long as all char are correct, casing doesn't matter)
Blog.objects.filter(name__contains='foo') #<QuerySet [<Blog: Food blog>]>


#Вывести названия всех статей и название блогов, которому они принадлежат
for entry in Entry.objects.all():
    print(entry.headline, entry.blog.name)

#Вывести все статьи блога с id=1
Blog.objects.get(pk=1).entry_set.all()  *2 db hits*
Entry.objects.filter(blog__id=1)        *1 db hit*

####################################
########## MANY TO MANY #########
####################################
#https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/


buff_entry = Entry.objects.get(headline__contains='buff') #<Entry: How to be buff>
buff_entry.authors.all() # <QuerySet [<Author: Karen>, <Author: Chad Douchebraun>]>

<>Adding new author to many to many relationship<>
chad = Author.objects.get(name__contains='chad') 
buff_entry.authors.add(chad)

#Query all Entries of Blog with id = 1 (From Entry model with blog id)
Entry.objects.filter(blog__id=1) <QuerySet [<Entry: PUMP NOK>, <Entry: How not to get poor>]>

#Query all entries of Blog (from Blog model)
food_blog = Blog.objects.get(id=2)
food_blog.entry_set.all()


#Many-to-many relationships can be queried using lookups across relationships:
Entry.objects.filter(blog__pk=2) <QuerySet [<Entry: Eat clean>]>
Entry.objects.filter(blog__name__contains='food') <QuerySet [<Entry: Eat clean>]>
*count*
Entry.objects.filter(blog__name__contains='food').count() 1
*distinct*
Entry.objects.filter(blog__name__contains='food').count().distinct() 1



<>Моя версия запроса 1<>
SELECT * 
FROM ENTRY
WHERE blog = 2

<>Моя версия запроса 2<>
SELECT * 
FROM ENTRY
WHERE id IN
    (SELECT id
    FROM Blog
    WHERE name LIKE '%food%')



######### SELECT RELATED #############
#valid for foreign key and one-to-one relationships
#You can specify many related tables, not just one
><standart lookup><
*Example 1*
# Hits the database.
food_blog = Blog.objects.get(name__contains='food')
# Hits the database again to get the related Editor object.
food_blog.editor               # <Editor: Nich Fooden>   
food_blog.editor.email         #'slfj@mgi.com'            

*Example 2*
for entry in Entry.objects.filter(blog__name__contains='food'):
    ...:     print(entry.headline, entry.blog.name)
#there is 4 entries, and we print two attributes, so there will 8 db hits to retrive info


><And here’s select_related lookup:><
 *Example 1*
# Hits the database.
food_blog = Blog.objects.select_related('editor').get(name__contains='food')
food_blog.editor               # <Editor: Nich Fooden>  

*Example 2*
# Find all the Entries where respective Blog has 'food' in his name
#this makes singele query intead of 8 in standard lookup
for entry in Entry.objects.select_related('blog').filter(blog__name__contains='food'):
    ...:     print(entry.headline, entry.blog.name)



############### PREFETCH RELATED ##################
#prefetch_related, on the other hand, does a separate lookup for each relationship, and does the ‘joining’ 
#in Python. This allows it to prefetch many-to-many and many-to-one objects, which cannot be done 
#using select_related, in addition to the foreign key and one-to-one relationships that are supported 
#by select_related."""
*standart lookup*  hits db 7 times
for entry in Entry.objects.all():
...:    for author in entry.authors.all():
...:    print(author.name, author.email)

<And here’s prefetch_related lookup:> hits db 2 times
*sdf*
In [11]: for entry in Entry.objects.prefetch_related('authors'):
    ...:     for author in entry.authors.all():
    ...:         print(author.name, author.email)

