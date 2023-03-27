
from random import choice as rc, randint
from faker import Faker
from app import app
from models import db, Camper, Activity, Signup

fake = Faker()

# CLIMBER, LOCATION, ROUTE, REVIEW(JOIN TABLE)

location

climbing_routes = [
    {
        "name": "El Capitan",
        "grading": "5.13d",
        "location": "Yosemite National Park, California, USA",
        "image": "https://www.outsideonline.com/wp-content/uploads/2021/06/10/El-Cap-Wall_Tristan-Gauthier_Unsplash.jpg",
        "style": "Multi-pitch"
    },
    {
        "name": "The Nose",
        "grading": "5.14a",
        "location": "Yosemite National Park, California, USA",
        "image": "https://www.climbing.com/.image/t_share/MTY1MTA1NDYyMjIyNzg0OTM2/el-capitan-the-nose.jpg",
        "style": "Multi-pitch"
    },
    {
        "name": "Biographie",
        "grading": "5.15a",
        "location": "Céüse, France",
        "image": "https://cdn-cms.f-static.net/uploads/2369633/800_5d868889f6d74.jpg",
        "style": "Sport"
    }
]

def make_routes():

    Route.query.delete()

    routes = []

    for route_dict in climbing_routes:
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