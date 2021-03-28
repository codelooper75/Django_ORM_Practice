#imports
from django.contrib.auth.models import User #to import User


#Retrive
roman = User.objects.get(username='roman')
Post.objects.filter(author=roman)

#create
roman = User.objects.get(username='roman') #get user object
post = Post.objects.create(author=roman, title='Sample title 3', text='Samle text 3')
post.save()
#or I can do it step by step
new_post = Post() #note don't try to save it like this. You will catch an error
new_post.author = roman
new_post.title = 'Post 4'
new_post.text = 'Post 4 text'
new_post.save()


#filtering by time
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now()) #lte  - less than or equals

#ordering
Post.objects.order_by('created_date') #ordre by created_date asc
Post.objects.order_by('-created_date') #ordre by created_date desc

#chaining
Post.objects.filter(title__contains='post').order_by('created_date')
