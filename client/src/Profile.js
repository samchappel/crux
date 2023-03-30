import React, { useState, useEffect } from "react";

function Profile() {
  const [climbs, setClimbs] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const climberId = sessionStorage.getItem("climberId");

    fetch('/climber/ticks')
      .then((res) => res.json())
      .then((data) => {
        setClimbs(data);
        setIsLoading(false);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <>
          <h2>My Climbs</h2>
          <ul>
            {climbs.map((climb) => (
              <li key={climb.id}>{climb.route.name}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default Profile;