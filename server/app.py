from flask import  request, make_response, session, abort, jsonify
from flask_restful import  Resource
from models import Climber, Location, Route, Review, Tick
from config import db, api, app


class Climbers(Resource):
    def get(self):
        climbers = [climber.to_dict() for climber in Climber.query.all()]
        response = make_response(
            climbers,
            200
        )
        return response
api.add_resource(Climbers, '/climbers')

class ClimberByID(Resource):
    def get(self, id):
        climber = Climber.query.filter_by(id=id).first()
        if not climber:
            abort(404, "Climber not found")
        climber_dict = climber.to_dict()
        response = make_response(
            climber_dict,
            200
        )
        return response
api.add_resource(ClimberByID, '/climber/<int:id>')

class Locations(Resource):
    def get(self):
        locations = [location.to_dict() for location in Location.query.all()]
        response = make_response(
            locations,
            200
        )
        return response
        
api.add_resource(Locations, '/locations')

class LocationByID(Resource):
    def get(self, id):
        location = location.query.filter_by(id=id).first()
        if not location:
            abort(404, "location not found")
        location_dict = location.to_dict()
        response = make_response(
            location_dict,
            200
        )
        return response
api.add_resource(LocationByID, '/location/<int:id>')    

class Routes(Resource):
    def get(self):
        routes = [route.to_dict() for route in Route.query.all()]
        response = make_response(
            routes,
            200
        )
        # response.headers['Content-Type'] = 'application/json'
        return response
api.add_resource(Routes, '/routes')

class RouteByID(Resource):
    def get(self, id):
        route = Route.query.filter_by(id=id).first()
        #if not route:
        #   abort(404, "Route not found")
        route_dict = route.to_dict(rules=("reviews", "-reviews.climber"))
        response = make_response(
            route_dict,
            200
        )
        return response
        
api.add_resource(RouteByID, '/routes/<int:id>')

def get_featured_routes():
    top_routes = db.session.query(Route, db.func.avg(Review.star_rating).label('average_star_rating')).join(Review).group_by(Route.id).order_by(db.func.avg(Review.star_rating).desc()).limit(10).all()
    return top_routes

class FeaturedRoutes(Resource):
    def get(self):
        featured_routes = get_featured_routes()
        return jsonify([{"route": route.to_dict(), "average_star_rating": average_star_rating} for route, average_star_rating in featured_routes])

api.add_resource(FeaturedRoutes, '/featured_routes')

class Reviews(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Review.query.all()]
        response = make_response(
            reviews,
            200
        )
        return response

    def post(self):
        try:
            data = request.get_json()
            review = Review(
                star_rating=data["star_rating"],
                safety_rating=data["safety_rating"],
                quality_rating=data["quality_rating"],
                comment=data["comment"],
                climber_id = session['climber_id'],
                route_id = int(data["route_id"])
            ) #how to attach climber and route, send IDs from front end in the request

            db.session.add(review)
            db.session.commit()
        except Exception as e:
            return make_response({
                "errors": [e.__str__()]
            }, 422)
        response = make_response(
            review.to_dict(),
            201
        )
        return response
api.add_resource(Reviews, '/reviews')

class ReviewByID(Resource):
    def get(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            abort(404, "Review not found")
        review_dict = review.to_dict()
        response = make_response(
            review_dict,
            200
        )
        return response

    def patch(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({'error': 'Review not found'}, 404)
        data= request.get_json()
        for attr in data:
            setattr(review, attr, data[attr])
        db.session.add(review)
        db.session.commit()

        return make_response(review.to_dict(), 202)

    def delete(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({"error": "review not found"}, 404)
        db.session.delete(review)
        db.session.commit()

        return make_response('', 204)

api.add_resource(ReviewByID, '/reviews/<int:id>')

class Ticks(Resource):
    def post(self):
        try:
            data = request.get_json()
            tick = Tick(
                date=data["date"],
                style=data["style"],
                notes=data.get("notes"),
                climber_id=data["climber_id"],
                route_id=data["route_id"]
            )
            db.session.add(tick)
            db.session.commit()
        except Exception as e:
            return make_response({
                "errors": [e.__str__()]
            }, 422)

        response = make_response(
            tick.to_dict(),
            201
        )
        return response

    def get(self):
        ticks = [tick.to_dict() for tick in Tick.query.all()]
        response = make_response(
            ticks,
            200
        )
        return response

api.add_resource(Ticks, '/ticks')


class TickByID(Resource):
    def get(self, id):
        tick = Tick.query.filter_by(id=id).first()
        if not tick:
            abort(404, "Tick not found")
        tick_dict = tick.to_dict()
        response = make_response(
            tick_dict,
            200
        )
        return response

    def patch(self, id):
        tick = Tick.query.filter_by(id=id).first()
        if not tick:
            return make_response({'error': 'Tick not found'}, 404)
        data = request.get_json()
        for attr in data:
            setattr(tick, attr, data[attr])
        db.session.add(tick)
        db.session.commit()

        return make_response(tick.to_dict(), 202)

    def delete(self, id):
        tick = Tick.query.filter_by(id=id).first()
        if not tick:
            make_response(
                {"error": "tick not found"},
                404
            )
        db.session.delete(tick)
        db.session.commit()

        return make_response('', 204)


api.add_resource(TickByID, '/ticks/<int:id>')

class ClimberTicks(Resource):
    def get(self):
        if 'climber_id' not in session:
            abort(401, "Unauthorized")
        climber_id = session['climber_id']
        ticks = Tick.query.filter_by(climber_id=climber_id).all()
        routes = [tick.route.to_dict() for tick in ticks]
        response = make_response(
            routes,
            200
        )
        return response

api.add_resource(ClimberTicks, '/climber/ticks')

class Signup(Resource):
    def post(self):
        form_json = request.get_json()
        new_climber = Climber(username=form_json['username'])
        #Hashes our password and saves it to _password_hash
        new_climber.password_hash = form_json['password']

        db.session.add(new_climber)
        db.session.commit()

        response = make_response(
            new_climber.to_dict(),
            201
        )
        return response
api.add_resource(Signup, '/signup')

class Login(Resource):
    def post(self):
        try:
            climber = Climber.query.filter_by(username=request.get_json()['username']).first()
            if climber.authenticate(request.get_json()['password']):
                session['climber_id'] = climber.id
                response = make_response(
                    climber.to_dict(),
                    200
                )
                return response
        except:
            abort(401, "Incorrect Username or Password")

api.add_resource(Login, '/login')

class AuthorizedSession(Resource):
    def get(self):
        try:
            climber = Climber.query.filter_by(id=session['climber_id']).first()
            response = make_response(
                climber.to_dict(),
        
                200
            )
            return response
        except:
            abort(401, "Unauthorized")

api.add_resource(AuthorizedSession, '/authorized')

class Logout(Resource):
    def delete(self):
        session['climber_id'] = None 
        response = make_response('',204)
        return response
api.add_resource(Logout, '/logout')


if __name__ == "__main__":
    app.run(port="5555", debug=True)