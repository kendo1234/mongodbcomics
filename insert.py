from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

# If no database is present with this name, it will be created
db = client['Physical_Comics']

marvel = db.marvel
# marvel_comic = {
#     'title':'Old Man Logan',
#     'writer': 'Mark Millar',
#     'artist': 'Steve McNiven'
# }
# result = marvel.insert_one(marvel_comic)
# print('One comic: {0}'.format(result.inserted_id))


# Find data
# brians_books = marvel.find({'writer': 'Brian Michael Bendis'})
# print(brians_books)

# Find all

marvel_books = db.marvel.find()
print(marvel_books)