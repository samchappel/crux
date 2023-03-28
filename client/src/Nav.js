import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const user = localStorage.getItem('user'); // Replace 'user' with specific key
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
            <Link to="/log_out" onClick={() => {
              localStorage.removeItem('user');
              setIsLoggedIn(false);
            }}>Log Out</Link>
          </>
        ) : (
          <Link to="/log_in">Log In/Sign Up</Link>
        )}
      </nav>
    </div>
  );
}

export default NavBar;