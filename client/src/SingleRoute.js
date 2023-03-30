import { useEffect, useState } from "react";
import { Link, useHistory, useParams } from "react-router-dom";


function SingleRoute({climber}){
    const[route, setRoute]= useState(null)
    const [isLoaded, setIsLoaded] = useState(false);
     const history = useHistory();

    const{ id } = useParams()
    
    useEffect(() => {
        console.log('in useEffect')
        fetch(`/routes/${id}`)
        .then((r)=> r.json())
        .then((route)=> {
            setRoute(route);
            setIsLoaded(true);
        });
    }, [id])
    
    if (!isLoaded) return <h1>Loading...</h1>;
    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const monthNames = [
            'January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December',
        ];
        
        const month = monthNames[date.getMonth()];
        const day = date.getDate();
        const year = date.getFullYear();
        
        return `${month} ${day}, ${year}`;
        };
    const { name, style, grade, image, location, reviews, ticks} = route
    const reviewsToDisplay = reviews.map((review)=> {
        return <div><p>star rating: {review.star_rating}</p>
        <p>safety rating: {review.safety_rating}</p>
        <p>quality rating: {review.quality_rating}</p>
        <p>comment: {review.comment}</p>
        <p>created at: {formatDate(review.created_at)}</p>
        {climber.id === review.climber_id ? (
            <Link to={`/review/${review.id}/edit`}>
            <p className="linkToEdit">Edit Review</p>
            </Link>
        ) : null}
        </div>
    });
    const addTick = ticks.map((tick) => {
        return <div><p>Date Ticked: {tick.date}</p>
        <p>Notes: {tick.notes}</p>
        </div>
    })

    return(
        <div className="single-route">
        <div className="single-nontext">
            <img className="single-image" src={image} alt={name} />
        </div>
        <div className="tick">
            <Link to={`/routes/${id}/ticks`}><p className="linkToTick">Add Tick</p></Link>
        </div>
        <div className="single-center">
        <h3 className="single-name">{name}</h3>
        <p>Style: {style}</p>
        <p>Grade: {grade}</p>
        <p>Location: {location.place} </p>
        {reviews === true ? <div><p>Reviews:</p>
        <p>{reviewsToDisplay}</p></div>
        : null}
        <p>Reviews:</p>
        <p>{addTick}</p>
        <p>{reviewsToDisplay}</p>
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