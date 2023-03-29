import { Link } from 'react-router-dom';

function ClimbingRoutesCard({ route }) {
    const { name, style, grade, image, id } = route;

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
          <div className="location">
            <p>Location:</p>
          </div>
        </div>
      </li>
    );
  }
  
  export default ClimbingRoutesCard;