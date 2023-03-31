import React, { useState, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';

function NavBar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const history = useHistory();
  
  useEffect(() => {
    fetch('/authorized')
      .then(res => {
        if (res.ok) {
          setIsLoggedIn(true);
        } else {
          setIsLoggedIn(false);
        }
      })
      .catch(error => console.error('Error checking auth status:', error));
  }, []);

  const handleLogout = () => {
    fetch('/logout', { method: 'DELETE' })
      .then(() => {
        setIsLoggedIn(false);
        history.push('/login');
      })
      .catch(error => console.error('Error logging out:', error));
  };

  return (
    <div className="nav-container">
      <nav className="nav-bar">
        <Link to="/featured_routes">Home</Link>
        <Link to="/routes">Routes</Link>
        <Link to="/submit">Add a Route</Link>
        {isLoggedIn ? (
          <>
            <Link to="/profile">Profile</Link>
            <Link to="/logout" onClick={handleLogout}>Log Out</Link>
          </>
        ) : (
          <Link to="/login">Log In/Sign Up</Link>
        )}
      </nav>
    </div>
  );
}

export default NavBar;