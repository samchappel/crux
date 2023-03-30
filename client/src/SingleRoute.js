import { useEffect, useState } from "react";
import { Link, useHistory, useParams } from "react-router-dom";

function SingleRoute() {
  const [route, setRoute] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const { id } = useParams();
  const history = useHistory();

  useEffect(() => {
    console.log("in useEffect");
    fetch(`http://localhost:5555/routes/${id}`)
      .then((r) => r.json())
      .then((route) => {
        setRoute(route);
        setIsLoaded(true);
      });
  }, [id]);

  if (!isLoaded) return <h1>Loading...</h1>;
  const { name, style, grade, image, location } = route;

  return (
    <div className="single-route">
      <div className="single-nontext">
        <img className="single-image" src={image} alt={name} />
      </div>
      <div className="single-center">
        <h3 className="single-name">{name}</h3>
        <p>Style: {style}</p>
        <p>Grade: {grade}</p>
        <p>Location: {location.place}</p>
        <Link to={`/routes/${id}/edit`}>
          <button>Edit This Route</button>
        </Link>
        <br />
        <button onClick={() => history.goBack()}>Back</button>
      </div>
    </div>
  );
}

export default SingleRoute;