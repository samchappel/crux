
from random import choice as rc, randint
#from faker import Faker
from app import app
from models import db, Climber, Location, Route, Review

#fake = Faker()

# CLIMBER, LOCATION, ROUTE, REVIEW(JOIN TABLE)

# Delete all existing data
# print('deleting all data')
# with app.app_context():
#     db.drop_all()
#     db.create_all()
# print('all data deleted')
# Climber data

print('creating climbers')
climbers_list = [
    {"username": "packDaddy", "email": "packD@climber.com", "password": "@samDAbest", "first_name": "Sam", "last_name": "C"},
    {"username": "hot_stove", "email": "stove_top@climber.com", "password": "@fireGripper", "first_name": "Steve", "last_name": "P"},
    {"username": "send_IT", "email": "chalky@climber.com", "password": "@sentDat", "first_name": "Ari", "last_name": "M"}
]
print('climbers created')

# Add climbers to database
def make_climbers():

    Climber.query.delete()

    climbers = []

    for climber_dict in climbers_list:
        climber = Climber(
            username=climber_dict["username"],
            email=climber_dict["email"],
            password=climber_dict["password"],
            first_name=climber_dict["first_name"],
            last_name=climber_dict["last_name"]
        )
        climbers.append(climber)

    db.session.add_all(climbers)
    db.session.commit()
print('climbers committed')
# Location data

print('creating locations')
locations_list = [   
    {"place": "Smith Rock", "crag_name": "The Dihedrals", "city": "Terrebonne", "state": "Oregon", "country": "USA"},    
    {"place": "Yosemite National Park", "crag_name": "Southwest Face", "city": "Mariposa County", "state": "California", "country": "USA"},    
    {"place": "Yosemite National Park", "crag_name": "El Capitan", "city": "Mariposa County", "state": "California", "country": "USA"},    
    {"place": "Céüse", "crag_name": "Secteur Biographie", "city": "Sigoyer", "state": "Hautes-Alpes", "country": "France"}]
print('locations created')

# Add locations to database
def make_locations():

    Location.query.delete()

    locations = []

    for location_dict in locations_list:
        location = Location(
            place=location_dict["place"],
            crag_name=location_dict["crag_name"],
            city=location_dict["city"],
            state=location_dict['state'],
            #image=location_dict["image"],
            country=location_dict["country"]
        )
        locations.append(location)

    db.session.add_all(locations)
    db.session.commit()
print('locations committed')

# Route data
print('creating routes')
routes_list = [    
    {"name": "To Bolt or Not to Be", "style": "Sport", "grade": "5.14a", "image": "https://cdn-files.apstatic.com/climb/110017364_medium_1494317655.jpg", "location_id": 1},    
    {"name": "The Mandala", "style": "Bouldering", "grade": "V12", "image": "https://cdn-files.apstatic.com/climb/111781832_medium_1494317576.jpg", "location_id": 1},    
    {"name": "The Chief", "style": "Trad", "grade": "5.11c", "image": "https://cdn-files.apstatic.com/climb/110015987_medium_1494317341.jpg", "location_id": 1},    
    {"name": "El Capitan", "style": "Multi-pitch", "grade": "5.13d", "image": "https://www.outsideonline.com/wp-content/uploads/2021/06/10/El-Cap-Wall_Tristan-Gauthier_Unsplash.jpg", "location_id": 3},    
    {"name": "The Nose", "style": "Multi-pitch", "grade": "5.14a", "image": "https://www.climbing.com/.image/t_share/MTY1MTA1NDYyMjIyNzg0OTM2/el-capitan-the-nose.jpg", "location_id": 2},    
    {"name": "Biographie", "style": "Sport", "grade": "5.15a", "image": "https://cdn-cms.f-static.net/uploads/2369633/800_5d868889f6d74.jpg", "location_id": 4} ]
print('routes created')

# Add routes to database
def make_routes():

    Route.query.delete()

    routes = []

    for route_dict in routes_list:
        route = Route(
            name=route_dict["name"],
            style=route_dict["style"],
            grade=route_dict["grade"],
            image=route_dict["image"],
            location_id=route_dict["location_id"]
        )
        routes.append(route)

    db.session.add_all(routes)
    db.session.commit()
print('routes committed')

print('creating reviews')
# Review data
reviews_list = [
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "Awesome climb!", "climber_id": 1, "route_id": 1},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Difficult problem, but rewarding.", "climber_id": 2, "route_id": 2},
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Good climb, but overrated in my opinion.", "climber_id": 3, "route_id": 3}
]
print('review created')

# Add reviews to database
def make_reviews():

    Review.query.delete()

    reviews = []

    for review_dict in reviews_list:
        review = Review(
            star_rating=review_dict["star_rating"],
            safety_rating=review_dict["safety_rating"],
            quality_rating=review_dict["quality_rating"],
            comment=review_dict["comment"],
            climber_id=review_dict["climber_id"],
            route_id=review_dict["route_id"]
        )
        reviews.append(review)

    db.session.add_all(reviews)
    db.session.commit()
print('review committed')

if __name__ == '__main__':
    with app.app_context():
        make_climbers()
        make_locations()
        make_routes()
        make_reviews()

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