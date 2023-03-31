import { useEffect, useState } from "react";
import { Link, useHistory, useParams } from "react-router-dom";


function SingleRoute({climber}){
    const[route, setRoute]= useState(null)
    const [isLoaded, setIsLoaded] = useState(false);
    const[ticks, setTicks] = useState(null)
    const history = useHistory();

    const{ id } = useParams()
    
    useEffect(() => {
        console.log('in useEffect');
        Promise.all([
            fetch(`/routes/${id}`).then((r) => r.json()),
            fetch(`/ticks`).then((r) => r.json()),
        ])
            .then(([route, ticks]) => {
            setRoute(route);
            setTicks(ticks);
            setIsLoaded(true);
            })
            .catch((error) => console.log(error));
        }, [id]);
    
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
    const { name, styleRoute, grade, image, location, reviews, routeId} = route
    console.log(reviews)
    const reviewsToDisplay = reviews.map((review)=> {
        console.log(review.id)
        console.log(review.created_at)
        return <div><p>star rating: {review.star_rating}</p>
        <p>safety rating: {review.safety_rating}</p>
        <p>quality rating: {review.quality_rating}</p>
        <p>comment: {review.comment}</p>
        <p>created at: {formatDate(review.created_at)}</p>
        {climber && climber.id === review.climber_id ? (
            <Link to={`/review/${review.id}/edit`}>
            <p className="linkToEdit">Edit Review</p>
            </Link>
        ) : null}
        </div>
    });
    console.log(ticks)
    const singleTick = ticks.filter((tick)=> climber && climber.id === tick.climber_id)
    console.log(singleTick)

    //const {climber_id, route_id, styleTick, date, notes } = tick
    // console.log(climber.id)
    // console.log(climber_id)
    // const addTick =
    // singleTick ? (
    //     <div>
    //         <p>Date Ticked: {singleTick.date}</p>
    //         <p>Style: {singleTick.styleTick}</p>
    //         <p>Notes: {singleTick.notes}</p>
    //     </div>
    // ) : null;

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
        <p>Style: {styleRoute}</p>
        <p>Grade: {grade}</p>
        <p>Location: {location.place} </p>
        {reviews === true ? <div><p>Reviews:</p>
        <p>{reviewsToDisplay}</p></div>
        : null}
        {singleTick ? (
        <div>
            <p>Date Ticked: {singleTick.date}</p>
            <p>Style: {singleTick.styleTick}</p>
            <p>Notes: {singleTick.notes}</p>
        </div>
        ) : null}
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