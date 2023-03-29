import React from 'react';
import { Link } from 'react-router-dom';

function ClimbingRoutesCard({ route }) {
  const { name, style, grade, image, id, location } = route;

  return (
    <li className="card">
      <div className="image">
        <Link to={`/routes/${id}`}>
          <img src={image} alt={name} />
        </Link>
      </div>
      <div className="center">
        <h3 className="name">{name}</h3>
        <p>{style}</p>
        <p>{grade}</p>
        <p>Location:{location.place}</p>
      </div>
    </li>
  );
}

export default ClimbingRoutesCard;