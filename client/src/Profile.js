import React, { useState, useEffect } from "react";
import { withRouter, Link } from "react-router-dom";

function Profile({ climber, history }) {
  const [ticks, setTicks] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [routes, setRoutes] = useState([]);
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    Promise.all([
      fetch('/ticks').then((res) => res.json()),
      fetch('/routes').then((res) => res.json()),
      fetch('/reviews').then((res) => res.json())
    ]).then(([ticksData, routesData, reviewsData]) => {
      setTicks(ticksData);
      setRoutes(routesData);
      setReviews(reviewsData);
      setIsLoading(false);
    }).catch((error) => console.log(error));
  }, []);

  const filteredTicks = ticks.filter((tick) => climber && climber.id === tick.climber_id);
  const ticksWithRouteName = filteredTicks.map((tick) => {
    const route = routes.find((route) => route.id === tick.route_id);
    return {
      ...tick,
      route_name: route ? route.name : null,
      route_image: route ? route.image : null,
    };
  });

  const handleMouseOver = (e) => {
    e.currentTarget.style.transform = 'scale(1.1)';
    e.currentTarget.style.transition = 'transform 0.2s';
  }

  const handleMouseOut = (e) => {
    e.currentTarget.style.transform = 'scale(1)';
    e.currentTarget.style.transition = 'transform 0.2s';
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const monthNames = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December',
    ];
    
    const month = monthNames[date.getMonth()];
    const day = date.getDate();
    const year = date.getFullYear();
    
    return `${month} ${day}, ${year}`;
    };

    const reviewsToDisplay = reviews
    .filter((review) => climber && climber.id === review.climber_id)
    .map((review) => {
      const route = routes.find((route) => route.id === review.route_id);
      const routeName = route ? route.name : null;
      const routeImage = route ? route.image : null;

      return (
        <li key={review.id} className="review-card">
          <div className="review-card__content">
            {routeName && <h3 className="review-card__title">{routeName}</h3>}
            {routeImage && <img className="review-card__image" src={routeImage} alt={routeName} />}
            <p className="review-card__rating">Star Rating: {review.star_rating}</p>
            <p className="review-card__rating">Safety Rating: {review.safety_rating}</p>
            <p className="review-card__rating">Quality Rating: {review.quality_rating}</p>
            <p className="review-card__comment">Comment: {review.comment}</p>
          </div>
        </li>
      );
    });

    return (
        <div>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <>
              <h2 className="profile-title">My Ticks</h2>
              {filteredTicks.length > 0 ? (
                <ul className="cards">
                  {ticksWithRouteName.map((tick) => (
                    <li key={tick.id} className="profile-card" onMouseOver={handleMouseOver} onMouseOut={handleMouseOut}>
                      <img className="profile-card__image" src={tick.route_image} alt={tick.route_name} />
                      <div className="profile-card__title">{tick.route_name}</div>
                      <div className="profile-card__date">{formatDate(tick.date)}</div>
                      <div className="profile-card__notes">My Notes: {tick.notes}</div>
                    </li>
                  ))}
                </ul>
              ) : (
                <p>There are no ticks to display - start sending to track your progress!</p>
              )}
              <div>
                <h2 className="profile-title">My Reviews</h2>
                <ul className="review-cards">{reviewsToDisplay}</ul>
              </div>
            </>
          )}
        </div>
      );
    }

export default withRouter(Profile);