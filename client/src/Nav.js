import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <div className="nav-container">
      <nav className="nav-bar">
        <Link to="/crux">Home</Link>
        <Link to="/routes">Routes</Link>
        <Link to="/submit">Add a Route</Link>
        <Link to="/profile">Profile</Link>
        <Link to="/log_in">Log In</Link>
      </nav>
    </div>
  );
}

export default NavBar;