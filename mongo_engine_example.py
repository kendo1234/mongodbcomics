import datetime
from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)



class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
post_1.save()       # This will perform an insert
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()       # This will perform an atomic edit on "title"
print(post_1.title)
