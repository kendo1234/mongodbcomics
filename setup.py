from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

# If no database is present with this name, it will be created
db = client['Physical_Comics']

marvel = db.marvel
marvel_comic = {
    'title':'Civil War',
    'writer': 'Brian Michael Bendis',
    'artist': 'Steve McNiven'
}
result = marvel.insert_one(marvel_comic)
print('One comic: {0}'.format(result.inserted_id))
