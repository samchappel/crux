import { useEffect, useState } from "react";
import { Link, useHistory, useParams } from "react-router-dom";
import Modal from 'react-modal';


function SingleRoute({climber}){
    const[route, setRoute]= useState(null)
    const [isLoaded, setIsLoaded] = useState(false);
    const[ticks, setTicks] = useState(null)
    const history = useHistory();
    const [showTickModal, setShowTickModal] = useState(false);
    const [flash, setFlash] = useState(false);
    const [send, setSend] = useState(false);
    const [attempt, setAttempt] = useState(false);
    const [leadStyle, setLeadStyle] = useState(null);
    const [boulderStyle, setBoulderStyle] = useState(null);
    const [leadSubstyle, setLeadSubstyle] = useState(null);
    const [tickDate, setTickDate] = useState("");
    const [tickStyle, setTickStyle] = useState("");
    const [tickNotes, setTickNotes] = useState("");

    const{ id } = useParams()
    
    useEffect(() => {
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

        const toggleTickModal = () => {
            setShowTickModal(prevState => !prevState);
          };

        function handleDeleteReview(id) {
            fetch(`/reviews/${id}`, {
              method: "DELETE",
            })
              .then((response) => {
                if (response.ok) {
                  // Delete successful, do something if necessary
                } else {
                  throw new Error("Failed to delete review");
                }
              })
              .catch((error) => {
                console.error(error);
              });
          }

          const { name, style, grade, image, location, reviews, routeId} = route


 
    // const reviewsToDisplay = reviews.map((review)=> {
    //     console.log(review.id)
    //     console.log(review.created_at)
    //     return <div><p>star rating: {review.star_rating}</p>
    //     <p>safety rating: {review.safety_rating}</p>
    //     <p>quality rating: {review.quality_rating}</p>
    //     <p>comment: {review.comment}</p>
    //     <p>created at: {formatDate(review.created_at)}</p>
    //     {climber && climber.id === review.climber_id ? (
    //         <Link to={`/review/${review.id}/edit`}>
    //         <p className="linkToEdit">Edit Review</p>
    //         </Link>
    //     ) : null}
    //     </div>
    // });

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

    let tickOptions;
    if (route.style === "sport" || route.style === "trad") {
      tickOptions = (
        <>
          <h4>Lead</h4>
          <label htmlFor="solo">
            <input
              type="radio"
              id="solo"
              name="leadStyle"
              value="solo"
              checked={leadStyle === "solo"}
              onChange={(e) => setLeadStyle(e.target.value)}
            />
            Solo
          </label>
          <label htmlFor="toprope">
            <input
              type="radio"
              id="toprope"
              name="leadStyle"
              value="toprope"
              checked={leadStyle === "toprope"}
              onChange={(e) => setLeadStyle(e.target.value)}
            />
            Toprope
          </label>
          <label htmlFor="follow">
            <input
              type="radio"
              id="follow"
              name="leadStyle"
              value="follow"
              checked={leadStyle === "follow"}
              onChange={(e) => setLeadStyle(e.target.value)}
            />
            Follow
          </label>
          <label htmlFor="lead">
            <input
              type="radio"
              id="lead"
              name="leadStyle"
              value="lead"
              checked={leadStyle === "lead"}
              onChange={(e) => setLeadStyle(e.target.value)}
            />
            Lead
          </label>
          {leadStyle === "lead" && (
            <>
              <label htmlFor="onsight">
                <input
                  type="radio"
                  id="onsight"
                  name="leadSubstyle"
                  value="onsight"
                  checked={leadSubstyle === "onsight"}
                  onChange={(e) => setLeadSubstyle(e.target.value)}
                />
                Onsight
              </label>
              <label htmlFor="flash">
                <input
                  type="radio"
                  id="flash"
                  name="leadSubstyle"
                  value="flash"
                  checked={leadSubstyle === "flash"}
                  onChange={(e) => setLeadSubstyle(e.target.value)}
                />
                Flash
              </label>
              <label htmlFor="redpoint">
                <input
                  type="radio"
                  id="redpoint"
                  name="leadSubstyle"
                  value="redpoint"
                  checked={leadSubstyle === "redpoint"}
                  onChange={(e) => setLeadSubstyle(e.target.value)}
                />
                Redpoint
              </label>
              <label htmlFor="pinkpoint">
                <input
                  type="radio"
                  id="pinkpoint"
                  name="leadSubstyle"
                  value="pinkpoint"
                  checked={leadSubstyle === "pinkpoint"}
                  onChange={(e) => setLeadSubstyle(e.target.value)}
                />
                Pinkpoint
              </label>
              <label htmlFor="fell-hung">
                <input
                  type="radio"
                  id="fell-hung"
                  name="leadSubstyle"
                  value="fell-hung"
                  checked={leadSubstyle === "fell-hung"}
                  onChange={(e) => setLeadSubstyle(e.target.value)}
                />
                Fell/Hung
              </label>
            </>
          )}
        </>
      );
    } else if (route.style === "boulder" || route.style === "dws") {
      tickOptions = (
        <>
          <h4>Boulder/DWS</h4>
      <label htmlFor="flash">
        <input type="radio" id="flash" name="boulderStyle" value="flash" checked={boulderStyle === "flash"} onChange={(e) => setBoulderStyle(e.target.value)} />
        Flash
      </label>
      <label htmlFor="send">
        <input type="radio" id="send" name="boulderStyle" value="send" checked={boulderStyle === "send"} onChange={(e) => setBoulderStyle(e.target.value)} />
        Send
      </label>
      <label htmlFor="attempt">
        <input type="radio" id="attempt" name="boulderStyle" value="attempt" checked={boulderStyle === "attempt"} onChange={(e) => setBoulderStyle(e.target.value)} />
        Attempt
      </label>
    </>
  );
} else {
  tickOptions = null;
}

function handleTickSubmit(e) {
    e.preventDefault();
    const newTick = {
      climber_id: climber.id,
      route_id: route.id,
      date: tickDate,
      style: tickStyle,
      notes: tickNotes,
    };
    fetch("/ticks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newTick),
    })
      .then((response) => response.json())
      .then((data) => {
        // do something with the response data, e.g. update state
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    toggleTickModal();
  }
return (

  <div className="single-route">
    <div className="single-nontext">
      <img className="single-image" src={image} alt={name} />
    </div>
    <div className="single-center">
      <h3 className="single-name">{name}</h3>
      <p>Style: {route.style}</p>
      <p>Grade: {grade}</p>
      <p>Location: {location.place} </p>
      <Link to={`/routes/${id}`}>
        <button>Edit This Route</button>
      </Link>
      <div>
        <Link to={`/routes/${id}/addreview`}>
          <button>Add Review</button>
        </Link>
      </div>
      <button onClick={toggleTickModal}>Add Tick</button>
      <Modal
  className="tick-modal"
  isOpen={showTickModal}
  onRequestClose={toggleTickModal}
  contentLabel="Add Tick Modal"
>
  <div className="tick-modal-content">
    <h2>Add Tick</h2>
    <button className="tick-close-button" onClick={toggleTickModal}>
      X
    </button>
    <form onSubmit={handleTickSubmit}>
      {tickOptions}
      <br />
      <label htmlFor="tickDate">Tick Date:</label>
      <input type="date" id="tickDate" name="tickDate" />
      <br />
      <label htmlFor="notes">Notes:</label>
      <br />
      <textarea id="notes" name="notes" rows="4" cols="50" value={tickNotes} onChange={(e) => setTickNotes(e.target.value)} />
      <br />
      <button>Add Tick</button>
    </form>
  </div>
</Modal>
      <br />
      <button onClick={() => history.goBack()}>Back</button>
    </div>
    <ul className="review-cards">
      {reviews.map((review) => (
        <li key={review.id} className="review-card">
          <div className="review-card__content">
            <h4 className="review-card__title">Review by Climber {review.climber_id}</h4>
            <p className="review-card__rating">Star Rating: {review.star_rating}</p>
            <p className="review-card__rating">Safety Rating: {review.safety_rating}</p>
            <p className="review-card__rating">Quality Rating: {review.quality_rating}</p>
            <p className="review-card__comment">Comment: {review.comment}</p>
            {climber && climber.id === review.climber_id ? (
              <div>
                <Link to={`/reviews/${review.id}/edit`}>
                  <button>Edit This Review</button>
                </Link>
                <br />
                <button onClick={() => handleDeleteReview(review.id)}>Delete Review</button>
              </div>
            ) : null}
          </div>
        </li>
        ))}
    </ul>
</div>
);
}

export default SingleRoute;

    