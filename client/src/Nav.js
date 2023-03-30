import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const user = sessionStorage.getItem('climber');
    if (user) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <div className="nav-container">
      <nav className="nav-bar">
        <Link to="/featured_routes">Home</Link>
        <Link to="/routes">Routes</Link>
        <Link to="/submit">Add a Route</Link>
        {isLoggedIn ? (
          <>
            <Link to="/profile">Profile</Link>
            <Link to="/logout" onClick={() => {
              sessionStorage.removeItem('climber');
              setIsLoggedIn(false);
            }}>Log Out</Link>
          </>
        ) : (
          <Link to="/login">Log In/Sign Up</Link>
        )}
      </nav>
    </div>
  );
}

export default NavBar;