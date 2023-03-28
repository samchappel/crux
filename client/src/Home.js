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

      return (
        <div>
          <h1>Welcome to Crux!</h1>
          <p>Check out some of our featured routes:</p>
          {/* Display featured routes */}
          {featuredRoutes.length > 0 ? (
            <ul>
              {featuredRoutes.map(({ route, average_star_rating }, index) => (
                <li key={index}>
                  <h3>{route.name}</h3>
                  <p>{route.grade}</p>
                  <p>{route.style}</p>
                  <p>Average Star Rating: {average_star_rating.toFixed(1)}</p>
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