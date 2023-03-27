
from random import choice as rc, randint
from faker import Faker
from app import app
from models import db, Climber, Location, Route, Review, db

fake = Faker()

# CLIMBER, LOCATION, ROUTE, REVIEW(JOIN TABLE)

# Delete all existing data
print('deleting all data')
db.drop_all()
db.create_all()
print('all data deleted')
# Climber data

print('creating climbers')
climbers = [
    {"username": "packDaddy", "email": "packD@climber.com", "password": "samDAbest", "first_name": "Sam", "last_name": "C"},
    {"username": "hot_stove", "email": "stove_top@climber.com", "password": "fireGripper", "first_name": "Steve", "last_name": "P"},
    {"username": "send_IT", "email": "chalky@climber.com", "password": "sentDat", "first_name": "Ari", "last_name": "M"}
]
print('climbers created')

# Add climbers to database
for climber in climbers:
    new_climber = Climber(**climber)
    db.session.add(new_climber)
    db.session.commit()
print('climbers committed')
# Location data

print('creating locations')
locations = [   
    {"place": "Smith Rock", "crag_name": "The Dihedrals", "city": "Terrebonne", "state": "Oregon", "country": "USA"},    
    {"place": "Yosemite National Park", "crag_name": "Southwest Face", "city": "Mariposa County", "state": "California", "country": "USA"},    
    {"place": "Yosemite National Park", "crag_name": "El Capitan", "city": "Mariposa County", "state": "California", "country": "USA"},    
    {"place": "Céüse", "crag_name": "Secteur Biographie", "city": "Sigoyer", "state": "Hautes-Alpes", "country": "France"}]
print('locations created')

# Add locations to database
for location in locations:
    new_location = Location(**location)
    db.session.add(new_location)
    db.session.commit()
print('locations committed')

# Route data
print('creating routes')
routes = [    
    {"name": "To Bolt or Not to Be", "style": "Sport", "grade": "5.14a", "image": "https://cdn-files.apstatic.com/climb/110017364_medium_1494317655.jpg", "location_id": 1},    
    {"name": "The Mandala", "style": "Bouldering", "grade": "V12", "image": "https://cdn-files.apstatic.com/climb/111781832_medium_1494317576.jpg"},    
    {"name": "The Chief", "style": "Trad", "grade": "5.11c", "image": "https://cdn-files.apstatic.com/climb/110015987_medium_1494317341.jpg"},    
    {"name": "El Capitan", "style": "Multi-pitch", "grade": "5.13d", "image": "https://www.outsideonline.com/wp-content/uploads/2021/06/10/El-Cap-Wall_Tristan-Gauthier_Unsplash.jpg"},    
    {"name": "The Nose", "style": "Multi-pitch", "grade": "5.14a", "image": "https://www.climbing.com/.image/t_share/MTY1MTA1NDYyMjIyNzg0OTM2/el-capitan-the-nose.jpg"},    
    {"name": "Biographie", "style": "Sport", "grade": "5.15a", "image": "https://cdn-cms.f-static.net/uploads/2369633/800_5d868889f6d74.jpg"}]
print('routes created')

# Add routes to database
for route in routes:
    new_route = Route(**route)
    db.session.add(new_route)
    db.session.commit()
print('routes committed')

print('creating reviews')
# Review data
reviews = [
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "Awesome climb!"},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Difficult problem, but rewarding."},
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Good climb, but overrated in my opinion."}
]
print('review created')

# Add reviews to database
for review in reviews:
    new_review = Review(**review)
    db.session.add(new_review)
    db.session.commit()
print('review created')

# climbing_routes = [
#     {
#         "name": "El Capitan",
#         "grading": "5.13d",
#         "location": "Yosemite National Park, California, USA",
#         "image": "https://www.outsideonline.com/wp-content/uploads/2021/06/10/El-Cap-Wall_Tristan-Gauthier_Unsplash.jpg",
#         "style": "Multi-pitch"
#     },
#     {
#         "name": "The Nose",
#         "grading": "5.14a",
#         "location": "Yosemite National Park, California, USA",
#         "image": "https://www.climbing.com/.image/t_share/MTY1MTA1NDYyMjIyNzg0OTM2/el-capitan-the-nose.jpg",
#         "style": "Multi-pitch"
#     },
#     {
#         "name": "Biographie",
#         "grading": "5.15a",
#         "location": "Céüse, France",
#         "image": "https://cdn-cms.f-static.net/uploads/2369633/800_5d868889f6d74.jpg",
#         "style": "Sport"
#     }
# ]

# def make_routes():

#     Route.query.delete()

#     routes = []

#     for route_dict in climbing_routes:
#         route = Route(
#             name=route_dict["name"],
#             style=route_dict["style"],
#             grade=route_dict["grade"],
#             image=route_dict["image"],
#             location_id=route_dict["location_id"]
#         )
#         routes.append(route)

#     db.session.add_all(routes)
#     db.session.commit()