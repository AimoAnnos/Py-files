import json

def load_db():
    with open('db.json', 'r') as f:
        return json.load(f)

#db = load_db() # voi kutsua muuttujana myös tässä filussa, mutta ehkä sekavaa
# print(load_db())

def save_db(db):
    with open('db.json', 'w') as f:
        return json.dump(db, f)  # dump-s = dump (convert into) string