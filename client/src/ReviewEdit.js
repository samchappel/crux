import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';

function ReviewEdit({climber}) { //{climber} add
    const history = useHistory();
    const {id} = useParams();  
    const [review, setReview] = useState({
        star_rating: '',
        safety_rating: '',
        quality_rating: '',
        comment: '',
        //locationPlace: ''
        });
        const [isLoaded, setIsLoaded] = useState(true);
        useEffect(()=>{
            console.log(id)
            fetch(`http://localhost:5555/reviews/${id}`)
            .then(res=>res.json())
            .then((data) => {
                setReview(data);
                setIsLoaded(true);
            })
        }, [id])

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: review,
        onSubmit: (values) => {
            fetch(`/reviews/${id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        setReview(data)
                        history.push(`/routes/${review.route_id}`)
                    })
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })


    if (!isLoaded) return <h1>Loading...</h1>;
    if ((climber&&climber.is_admin === false) || (!climber)) {
        return <h1>Cannot edit this Review</h1>
    } else {
        return (
            <>
                <div className='new-review-form'>
                    <h2 className='review-title'>Edit Review</h2>
                    <form onSubmit={formik.handleSubmit} >
                        <label >Star Rating:</label>
                        <input type="text"  name="star_rating" value={formik.values.star_rating} onChange={formik.handleChange} />
                        <br></br>
                        <label >Safety Rating:</label>
                        <input type="text"  name="safety_rating" value={formik.values.safety_rating} onChange={formik.handleChange} />
                        <br></br>
                        <label >Quality Rating:</label>
                        <input type="text"  name="quality_rating" value={formik.values.quality_rating} onChange={formik.handleChange} />
                        <br></br>
                        <label >Comments:</label>
                        <input type="text"  name="comment" value={formik.values.comment} onChange={formik.handleChange} />
                        <br></br>
                        <button type="submit" value='Save'>Update</button>
                        <button type="button" onClick={() => history.goBack()}>Cancel</button>
                    </form>
                </div>
            </>
        );
    }
}

export default ReviewEdit