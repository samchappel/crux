
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
    {"username": "packDaddy", "email": "packD@climber.com", "password": "@samDAbest", "first_name": "Sam", "last_name": "Chappel"},
    {"username": "hot_stove", "email": "stove_top@climber.com", "password": "@fireGripper", "first_name": "Steve", "last_name": "Passarelli"},
    {"username": "send_IT", "email": "chalky@climber.com", "password": "@sentDat", "first_name": "Ari", "last_name": "Marz"},
    {"username": "KyleBigMits", "email": "kyle@boulderingisdumb.com", "password": "@Top0ut23", "first_name": "Kyle", "last_name": "Wehrung"},
    {"username": "NickRocksOn", "email": "nick@rockymoves.com", "password": "@CragHopper", "first_name": "Nick", "last_name": "Johnson"},
    {"username": "PalmquistGrip", "email": "emiley@holdtight.com", "password": "@PalmquistPower", "first_name": "Emiley", "last_name": "Palmquist"},
    {"username": "TopherSummit", "email": "topher@nottopher.com", "password": "@LudlowLedge", "first_name": "Topher", "last_name": "Ludlow"},
    {"username": "ChungDyno", "email": "terrence@dynojumps.com", "password": "@ChungChampion", "first_name": "Terrence", "last_name": "Chung"},
    {"username": "SchneiderSend", "email": "kyle@schneidersend.com", "password": "@SendItSchneider", "first_name": "Kyle", "last_name": "Schneider"},
    {"username": "BiancaBeta", "email": "bianca@routeplanning.com", "password": "@AspinAdvice", "first_name": "Bianca", "last_name": "Aspin"},
    {"username": "DianaClimbs", "email": "diana@mountaindancer.com", "password": "@LinUpTheWall", "first_name": "Diana", "last_name": "Lin"},
    {"username": "PattieGonia", "email": "patty@stronggrip.com", "password": "@EatAssBro", "first_name": "Patty", "last_name": "Hughes"},
    {"username": "BrettBearGrip", "email": "brett@bearhugholds.com", "password": "@DeBearStrength", "first_name": "Brett", "last_name": "de Bear"},
    {"username": "LynnHill", "email": "lynn@itgoesboys.com", "password": "@TheNoseInADay", "first_name": "Lynn", "last_name": "Hill"},
    {"username": "SharmaFan", "email": "chris@sharmafan.com", "password": "@KingLines", "first_name": "Chris", "last_name": "Sharma"},
    {"username": "CaldwellCrusher", "email": "tommy@crushingprojects.com", "password": "@DawnWall", "first_name": "Tommy", "last_name": "Caldwell"},
    {"username": "HonnoldSolo", "email": "alex@nohandsneeded.com", "password": "@FreeSolo", "first_name": "Alex", "last_name": "Honnold"},
    {"username": "OndraSend", "email": "adam@silentroars.com", "password": "@Silence9c", "first_name": "Adam", "last_name": "Ondra"},
    {"username": "SashaDiggs", "email": "sasha@inspirationontherocks.com", "password": "@VerticalWorld", "first_name": "Sasha", "last_name": "DiGiulian"},
    {"username": "MargoTheCrusher", "email": "margo@breakingbarriers.com", "password": "@Grade15", "first_name": "Margo", "last_name": "Hayes"},
    {"username": "PringlePower", "email": "ethan@sendtrain.com", "password": "@BatHangAlways", "first_name": "Ethan", "last_name": "Pringle"},
    {"username": "MegosMachine", "email": "alex@precisiongerman.com", "password": "@FastClimb", "first_name": "Alexander", "last_name": "Megos"},
    {"username": "BrookeRaboutou", "email": "brooke@climbingprodigy.com", "password": "@ClimbYoung", "first_name": "Brooke", "last_name": "Raboutou"},
    {"username": "HighballNina", "email": "nina@highballqueen.com", "password": "@ToppingOutHigh", "first_name": "Nina", "last_name": "Williams"},
    {"username": "PuccioPower", "email": "alex@boulderingbeast.com", "password": "@StrongClimbs", "first_name": "Alex", "last_name": "Puccio"}
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
    {"place": "Smith Rock", "city": "Terrebonne", "state": "Oregon", "country": "USA"},
    {"place": "Yosemite National Park", "city": "Mariposa", "state": "California", "country": "USA"},
    {"place": "Céüse", "city": "Sigoyer", "state": "Provence-Alpes-Côte d'Azur", "country": "France"},
    {"place": "Mallorca", "city": "Balearic Islands", "state": "Balearic Islands", "country": "Spain"},
    {"place": "Dumbarton Rock", "city": "Dumbarton", "state": "West Dunbartonshire", "country": "Scotland"},
    {"place": "Black Canyon of the Gunnison", "city": "Montrose", "state": "Colorado", "country": "USA"},
    {"place": "Flatanger Cave", "city": "Flatanger", "state": "Trøndelag", "country": "Norway"},
    {"place": "Sardinia", "city": "Nuoro", "state": "Sardinia", "country": "Italy"},
    {"place": "The Hurricave", "city": "Hanshelleren", "state": "Nordland", "country": "Norway"},
    {"place": "The Diamond", "city": "Estes Park", "state": "Colorado", "country": "USA"},
    {"place": "Squamish", "city": "Squamish", "state": "British Columbia", "country": "Canada"},
    {"place": "La Cova de l'Ocell", "city": "Santa Linya", "state": "Catalonia", "country": "Spain"}]
print('locations created')

# Add locations to database
def make_locations():

    Location.query.delete()

    locations = []

    for location_dict in locations_list:
        location = Location(
            place=location_dict["place"],
            # crag_name=location_dict["crag_name"],
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
    {"name": "To Bolt or Not to Be", "style": "Sport", "grade": "5.14a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},    
    {"name": "The Mandala", "style": "Bouldering", "grade": "V12", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},    
    {"name": "The Chief", "style": "Trad", "grade": "5.11c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},    
    {"name": "El Capitan", "style": "Multi-pitch", "grade": "5.13d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 3},    
    {"name": "The Nose", "style": "Multi-pitch", "grade": "5.14a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 2},    
    {"name": "Biographie", "style": "Sport", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "Dreamcatcher", "style": "Sport", "grade": "5.14d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "La Dura Dura", "style": "Sport", "grade": "5.15c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Jumbo Love", "style": "Sport", "grade": "5.15b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Perfecto Mundo", "style": "Sport", "grade": "5.15c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 12},
    {"name": "Es Pontas", "style": "Deep Water Solo", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 5},
    {"name": "The Salathe Wall", "style": "Multi-pitch", "grade": "5.13b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 3},
    {"name": "Rhapsody", "style": "Trad", "grade": "E11 7a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 6},
    {"name": "The Bachar-Yerian", "style": "Trad", "grade": "5.11d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "The Diamond", "style": "Trad", "grade": "5.14a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 7},
    {"name": "Leviathan", "style": "Sport", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Silence", "style": "Sport", "grade": "5.15d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 8},
    {"name": "La Rambla", "style": "Sport", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "La Planta de Shiva", "style": "Sport", "grade": "5.15b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "Perfecto Mundo", "style": "Sport", "grade": "5.15c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "La Dura Dura", "style": "Sport", "grade": "5.15c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "La Rambla Extension", "style": "Sport", "grade": "5.15b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "Bad Girls Club", "style": "Bouldering", "grade": "V10", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Terre de Sienne", "style": "Sport", "grade": "5.14b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 9},
    {"name": "The Path", "style": "Sport", "grade": "5.14a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Algorithm", "style": "Sport", "grade": "5.14d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 10},
    {"name": "Shadowboxing", "style": "Sport", "grade": "5.14d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Dihedral Wall", "style": "Trad", "grade": "5.14a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 3},
    {"name": "The Dawn Wall", "style": "Multi-pitch", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 2},
    {"name": "The Reticent Wall", "style": "Trad", "grade": "5.13c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 3},
    {"name": "The Emperor's New Clothes", "style": "Sport", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "Kaleidoscope", "style": "Sport", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "The Reckoning", "style": "Sport", "grade": "5.14d", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "The Edge of Time", "style": "Trad", "grade": "5.12a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 11},
    {"name": "La Voie Petit", "style": "Trad", "grade": "5.13c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 3},
    {"name": "La Capella", "style": "Sport", "grade": "5.15b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "Blackbeard's Tears", "style": "Sport", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "The Fly", "style": "Bouldering", "grade": "V13", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "King Line", "style": "Bouldering", "grade": "V14", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "The Grand Illusion", "style": "Sport", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "La Fabela pa la Enmienda", "style": "Sport", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 9},
    {"name": "Cobra Crack", "style": "Trad", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 12},
    {"name": "The Shield", "style": "Big Wall", "grade": "VI 5.13b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 3},
    {"name": "Ali Hulk Sit Start Extension Total", "style": "Bouldering", "grade": "V16", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 13},
    {"name": "La Esencia de la Resistencia", "style": "Sport", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "La Fuerza de la Gravedad", "style": "Sport", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "The Kaukulator", "style": "Trad", "grade": "5.12c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 1},
    {"name": "La Sportiva", "style": "Sport", "grade": "5.14b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "Esclatamasters", "style": "Sport", "grade": "5.15a", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4},
    {"name": "El Bon Combat", "style": "Sport", "grade": "5.15b", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 8},
    {"name": "La Fabela", "style": "Sport", "grade": "5.14c", "image": "https://images.squarespace-cdn.com/content/v1/5167372ce4b0f61ca31021ea/1449250741985-I1J6P05WJAHIJCSV6R65/image-asset.jpeg?format=500w", "location_id": 4}
    ]
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
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "Awesome climb! The route was challenging but manageable, and the view from the top was absolutely stunning.", "climber_id": 21, "route_id": 5},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Difficult problem, but rewarding. The holds were tricky to find, but once I did, the sequence was fun to execute.", "climber_id": 11, "route_id": 37},
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Good climb, but overrated in my opinion. The crux move was harder than expected, but the rest of the route was fairly straightforward.", "climber_id": 5, "route_id": 28},
    {"star_rating": 2, "safety_rating": 1, "quality_rating": 2, "comment": "Not a great climb. The holds were sharp and the route was poorly bolted.", "climber_id": 17, "route_id": 14},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely amazing climb! The route was well-maintained and the moves flowed together seamlessly.", "climber_id": 8, "route_id": 42},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Great climb, but a bit tough for the grade. The crux move required a lot of body tension and balance.", "climber_id": 23, "route_id": 9},
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Decent climb, but a bit sketchy in places. The rock was loose in a few spots and there were some runouts.", "climber_id": 14, "route_id": 31},
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "One of the best climbs I've ever done! The route was technical and challenging, but not too hard. Definitely worth doing!", "climber_id": 9, "route_id": 6},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Solid climb, with some fun moves. The crux move was a bit reachy, but still manageable.", "climber_id": 16, "route_id": 22},
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Decent climb, but a bit contrived. The route forced me to use some awkward moves that didn't feel natural.", "climber_id": 19, "route_id": 44},
    {"star_rating": 2, "safety_rating": 1, "quality_rating": 2, "comment": "Not a great climb. The holds were polished and slippery, and the route was poorly designed.", "climber_id": 4, "route_id": 16},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Incredible climb! The route was well-bolted and the moves were exciting. A must-do for any climber!", "climber_id": 7, "route_id": 33},
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 5, "comment": "A classic climb with great movement and excellent protection. The crux sequence was challenging but doable.", "climber_id": 12, "route_id": 8},
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "This climb was just okay. The route felt a bit forced and the moves weren't very interesting.", "climber_id": 18, "route_id": 25},
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "An absolute gem of a climb. The route was steep and sustained with plenty of interesting moves. Highly recommended!", "climber_id": 3, "route_id": 14},
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 3, "comment": "Not the best climb. The rock was loose in places and the moves were uninspiring.", "climber_id": 22, "route_id": 46},
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "A fun climb with good exposure. The crux move was tricky but well-protected.", "climber_id": 14, "route_id": 19},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "One of the best climbs I've ever done. The route was sustained and technical with a few cruxy moves. Definitely worth doing!", "climber_id": 1, "route_id": 3},
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 2, "comment": "Not the most enjoyable climb. The rock was chossy and the route lacked flow.", "climber_id": 20, "route_id": 49},
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "A solid climb with some interesting moves. The rock was a bit slick in places, but overall a good experience.", "climber_id": 10, "route_id": 29},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "An amazing climb with breathtaking views. The exposure was intense and the moves were exhilarating.", "climber_id": 6, "route_id": 36},
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "A disappointing climb. The route was dirty and poorly maintained, and the moves were uninspired.", "climber_id": 17, "route_id": 45},
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 4, "comment": "Challenging climb, but worth the effort.", "climber_id": 8, "route_id": 11},
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "A classic route with amazing views.", "climber_id": 16, "route_id": 22},
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 3, "comment": "Too easy and boring for my taste.", "climber_id": 4, "route_id": 14},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "A perfect climb with an epic finish!", "climber_id": 23, "route_id": 31},    
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Decent climb, but nothing special.", "climber_id": 12, "route_id": 19},    
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 5, "comment": "Tricky moves on this one, but it's a great challenge.", "climber_id": 9, "route_id": 47},    
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 1, "comment": "I did not enjoy this route at all.", "climber_id": 3, "route_id": 6},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "One of the best climbs I've ever done!", "climber_id": 19, "route_id": 41},    
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "A fun and challenging climb with great scenery.", "climber_id": 14, "route_id": 26},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "A decent climb, but not very memorable.", "climber_id": 6, "route_id": 17},
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "A fun climb with some challenging sections.", "climber_id": 10, "route_id": 29},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Decent route, but a bit too crowded for my taste.", "climber_id": 2, "route_id": 9}, 
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely amazing climb with breathtaking views!", "climber_id": 22, "route_id": 43},    
    {"star_rating": 2, "safety_rating": 1, "quality_rating": 3, "comment": "Not a fan of this route, felt unsafe in some parts.", "climber_id": 7, "route_id": 15},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "This climb had everything - technical sections, exposure, and stunning views!", "climber_id": 18, "route_id": 39},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "A great route with a tricky crux move.", "climber_id": 13, "route_id": 24},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "An average climb with no standout features.", "climber_id": 5, "route_id": 12},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "This climb was a true adventure with some amazing exposure!", "climber_id": 20, "route_id": 46},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "A solid climb with some interesting moves.", "climber_id": 15, "route_id": 32},    
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 2, "comment": "Not a great route, would not recommend.", "climber_id": 1, "route_id": 8},
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "A challenging climb with great views at the top.", "climber_id": 11, "route_id": 36},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "One of the best climbs I've ever done - amazing!", "climber_id": 23, "route_id": 47},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "An okay route, nothing special.", "climber_id": 6, "route_id": 14},    
    {"star_rating": 2, "safety_rating": 1, "quality_rating": 2, "comment": "Unsafe climb with poor quality rock.", "climber_id": 9, "route_id": 20},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely stunning climb with a perfect mix of technical and endurance challenges.", "climber_id": 17, "route_id": 41},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "A solid route with a tricky crux move - loved it!", "climber_id": 12, "route_id": 27},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Some sections felt unsafe, but overall an okay climb.", "climber_id": 4, "route_id": 13},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "This climb was a true adventure with some amazing exposure and beautiful scenery!", "climber_id": 19, "route_id": 45},    
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "A challenging route with some fun and technical moves.", "climber_id": 14, "route_id": 33},    
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 2, "comment": "Not a great climb, the holds were polished and the route felt uninspired.", "climber_id": 3, "route_id": 10},
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 5, "comment": "A classic climb with great movement and excellent protection. The crux sequence was challenging but doable.", "climber_id": 12, "route_id": 8},
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "This climb was just okay. The route felt a bit forced and the moves weren't very interesting.", "climber_id": 18, "route_id": 25},
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "An absolute gem of a climb. The route was steep and sustained with plenty of interesting moves. Highly recommended!", "climber_id": 3, "route_id": 14},
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 3, "comment": "Not the best climb. The rock was loose in places and the moves were uninspiring.", "climber_id": 22, "route_id": 46},
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "A fun climb with good exposure. The crux move was tricky but well-protected.", "climber_id": 14, "route_id": 19},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "One of the best climbs I've ever done. The route was sustained and technical with a few cruxy moves. Definitely worth doing!", "climber_id": 1, "route_id": 3},
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 2, "comment": "Not the most enjoyable climb. The rock was chossy and the route lacked flow.", "climber_id": 20, "route_id": 49},
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "A solid climb with some interesting moves. The rock was a bit slick in places, but overall a good experience.", "climber_id": 10, "route_id": 29},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "An amazing climb with breathtaking views. The exposure was intense and the moves were exhilarating.", "climber_id": 6, "route_id": 36},
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "A disappointing climb. The route was dirty and poorly maintained, and the moves were uninspired.", "climber_id": 17, "route_id": 45},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 5, "comment": "Great route with amazing views!", "climber_id": 17, "route_id": 13},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 4, "comment": "Challenging but fun climb!", "climber_id": 8, "route_id": 43},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely perfect climb!", "climber_id": 4, "route_id": 20},    
    {"star_rating": 2, "safety_rating": 1, "quality_rating": 3, "comment": "Disappointing climb, needs better maintenance", "climber_id": 14, "route_id": 31},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Unforgettable climb, highly recommend!", "climber_id": 23, "route_id": 11},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Solid climb with a challenging crux!", "climber_id": 3, "route_id": 46},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Average climb, nothing special", "climber_id": 19, "route_id": 25},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "Epic climb with amazing exposure!", "climber_id": 7, "route_id": 8},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Enjoyable climb with a great mix of holds", "climber_id": 6, "route_id": 33},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 2, "comment": "Underwhelming climb, not worth the effort", "climber_id": 16, "route_id": 18},
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 5, "comment": "Fun and challenging climb with good variety of holds", "climber_id": 12, "route_id": 22},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "One of the best climbs I've ever done, amazing!", "climber_id": 24, "route_id": 3},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 4, "comment": "Difficult climb with some loose rock, but worth it for the view", "climber_id": 9, "route_id": 41},
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "Disappointing climb, poorly maintained", "climber_id": 21, "route_id": 17},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Solid climb, great for working on technique", "climber_id": 5, "route_id": 36},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Incredible climb, the exposure is unreal!", "climber_id": 1, "route_id": 7},    
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Good climb, but overrated in my opinion", "climber_id": 13, "route_id": 29},    
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Challenging climb with some tricky moves, but rewarding", "climber_id": 20, "route_id": 48},    
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 2, "comment": "Not a very interesting climb, wouldn't do it again", "climber_id": 6, "route_id": 15},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "Absolutely perfect climb, can't wait to do it again!", "climber_id": 18, "route_id": 9},
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "The views from the top were breathtaking!", "climber_id": 14, "route_id": 9},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 4, "comment": "A challenging climb, but worth it.", "climber_id": 7, "route_id": 19},    
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "Great route for practicing crack climbing!", "climber_id": 23, "route_id": 12},    
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "I didn't enjoy this climb very much.", "climber_id": 2, "route_id": 31},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "This climb was an absolute blast!", "climber_id": 9, "route_id": 42},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 3, "comment": "Good climb, but the hold at the top needs to be fixed.", "climber_id": 17, "route_id": 24},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Not my favorite climb, but still fun.", "climber_id": 12, "route_id": 47},    
    {"star_rating": 2, "safety_rating": 1, "quality_rating": 2, "comment": "I felt very unsafe on this route.", "climber_id": 8, "route_id": 15},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 4, "comment": "The perfect climb for a beautiful day!", "climber_id": 3, "route_id": 33},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 5, "comment": "A classic route that every climber should try!", "climber_id": 21, "route_id": 6},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Great climb, loved the technical moves!", "climber_id": 14, "route_id": 48},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 4, "comment": "Fantastic climb, stunning views at the top.", "climber_id": 2, "route_id": 12},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Not my favorite climb, felt a bit dangerous.", "climber_id": 7, "route_id": 24},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely perfect climb, loved every minute of it!", "climber_id": 18, "route_id": 8},    
    {"star_rating": 2, "safety_rating": 4, "quality_rating": 3, "comment": "A bit disappointed with this climb, not as fun as I thought it would be.", "climber_id": 9, "route_id": 31},    
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 5, "comment": "Challenging climb, but the safety measures were great and the view at the top was incredible.", "climber_id": 22, "route_id": 16},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 4, "comment": "One of the best climbs I've ever done, will definitely be back!", "climber_id": 5, "route_id": 44},    
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Decent climb, but nothing special.", "climber_id": 16, "route_id": 21},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Incredible climb, the views were breathtaking!", "climber_id": 1, "route_id": 42},    
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 4, "comment": "Tough climb, but the challenge was worth it.", "climber_id": 13, "route_id": 29},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 5, "comment": "Fun climb with great views!", "climber_id": 18, "route_id": 13},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 4, "comment": "Challenging route but well worth it.", "climber_id": 7, "route_id": 45},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Not the best climb, but still enjoyable.", "climber_id": 2, "route_id": 29},    
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 5, "comment": "Amazing climb, highly recommend!", "climber_id": 12, "route_id": 18},    
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "Not my cup of tea, but some may enjoy it.", "climber_id": 23, "route_id": 7},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 4, "comment": "Loved this climb, great moves!", "climber_id": 15, "route_id": 33},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Decent climb, not too challenging.", "climber_id": 8, "route_id": 11},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "One of the best climbs I've done!", "climber_id": 4, "route_id": 48},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Solid climb, would recommend.", "climber_id": 19, "route_id": 22},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Not bad, but nothing special either.", "climber_id": 6, "route_id": 14},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 5, "comment": "Great climb, challenging moves!", "climber_id": 16, "route_id": 9},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 4, "comment": "Beautiful views, awesome climb!", "climber_id": 3, "route_id": 41},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Not my favorite route, but still a good climb.", "climber_id": 9, "route_id": 22},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely incredible climb, highly recommended!", "climber_id": 4, "route_id": 12},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Solid climb with good holds.", "climber_id": 7, "route_id": 33},    
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 2, "comment": "Disappointing climb, not very challenging.", "climber_id": 20, "route_id": 18},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Average climb, nothing special.", "climber_id": 12, "route_id": 27},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "One of the best climbs I've ever done, amazing!", "climber_id": 1, "route_id": 45},   
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 3, "comment": "Challenging climb, but safety gear is a must.", "climber_id": 19, "route_id": 7},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Stunning climb, a must-do for any experienced climber!", "climber_id": 6, "route_id": 48},
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely stunning climb!", "climber_id": 15, "route_id": 49},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Average climb, not very challenging.", "climber_id": 2, "route_id": 12},    
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "Great climb, definitely recommended!", "climber_id": 18, "route_id": 8},    
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "Disappointing climb, not worth the effort.", "climber_id": 4, "route_id": 41},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "Unbelievable views, truly breathtaking climb!", "climber_id": 22, "route_id": 32},    
    {"star_rating": 3, "safety_rating": 3, "quality_rating": 3, "comment": "Decent climb, but nothing special.", "climber_id": 6, "route_id": 16},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Challenging climb, but worth it for the sense of accomplishment!", "climber_id": 13, "route_id": 27},    
    {"star_rating": 2, "safety_rating": 2, "quality_rating": 3, "comment": "Poorly maintained climb, not very enjoyable.", "climber_id": 20, "route_id": 9},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Fun climb, great for a day trip!", "climber_id": 8, "route_id": 22},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Incredible climb, a must-do for experienced climbers!", "climber_id": 12, "route_id": 44},
    {"star_rating": 4, "safety_rating": 3, "quality_rating": 5, "comment": "Great climb with spectacular views!", "climber_id": 16, "route_id": 22},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 4, "comment": "Challenging route, but the views made it worth it.", "climber_id": 7, "route_id": 42},    
    {"star_rating": 3, "safety_rating": 2, "quality_rating": 3, "comment": "Not the most exciting climb, but good for beginners.", "climber_id": 12, "route_id": 11},    
    {"star_rating": 4, "safety_rating": 4, "quality_rating": 4, "comment": "Enjoyed this climb, but a bit too crowded.", "climber_id": 9, "route_id": 33},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Amazing climb, one of the best I've ever done!", "climber_id": 24, "route_id": 18},    
    {"star_rating": 2, "safety_rating": 3, "quality_rating": 2, "comment": "Not very challenging, but a good workout.", "climber_id": 3, "route_id": 7},    
    {"star_rating": 5, "safety_rating": 5, "quality_rating": 5, "comment": "Absolutely stunning climb with an epic finish!", "climber_id": 18, "route_id": 48},    
    {"star_rating": 3, "safety_rating": 4, "quality_rating": 3, "comment": "Decent climb, but nothing to write home about.", "climber_id": 5, "route_id": 27},    
    {"star_rating": 4, "safety_rating": 5, "quality_rating": 4, "comment": "Loved the technical challenges on this climb!", "climber_id": 19, "route_id": 14},    
    {"star_rating": 5, "safety_rating": 4, "quality_rating": 5, "comment": "The perfect climb for adrenaline junkies!", "climber_id": 21, "route_id": 49}
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