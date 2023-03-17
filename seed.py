from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# An alternative if you don't want to drop
# and recreate your tables:
# Pet.query.delete()

#Add pets

hunter = Pet(pet_name='Hunter', species='Dog', photo_url="", age="Baby", 
            notes="This is a cute puppy", available="True")
sophie = Pet(pet_name='Sophie', species='Cat', photo_url="", age="Senior", 
            notes="", available="False") 

# Add new objects to session, so they'll persist
db.session.add(hunter)
db.session.add(rick)

#commit
db.session.commit()
