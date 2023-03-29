import React, { useState, useEffect } from "react";

function Home() {
  const [featuredRoutes, setFeaturedRoutes] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/featured_routes")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.status}`);
        }
        return response.json();
      })
      .then(setFeaturedRoutes)
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleMouseOver = (e) => {
    e.currentTarget.style.transform = 'scale(1.1)';
    e.currentTarget.style.transition = 'transform 0.2s';
  }

  const handleMouseOut = (e) => {
    e.currentTarget.style.transform = 'scale(1)';
    e.currentTarget.style.transition = 'transform 0.2s';
  }

  return (
    <div>
      <h1>Welcome to Crux!</h1>
      <p>Check out some of our featured routes:</p>
      {/* Display featured routes */}
      {featuredRoutes.length > 0 ? (
        <ul className="cards">
          {featuredRoutes.map(({ route, average_star_rating }, index) => (
            <li key={index} className="card" onMouseOver={handleMouseOver} onMouseOut={handleMouseOut}>
              <div className="image">
                <img src={route.image} alt={route.name} />
              </div>
              <div className="center">
                <h3>{route.name}</h3>
                <p>{route.grade}</p>
                <p>{route.style}</p>
                <p>Average Star Rating: {average_star_rating.toFixed(1)}</p>
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default Home;