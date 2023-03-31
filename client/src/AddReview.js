import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';


function AddReview() { //{climber} add
    const history = useHistory();
    const {id} = useParams();  
    const [review, setReview] = useState({
        StarRating: '',
        SafetyRating: '',
        QualityRating: '',
        Comment: '',
        RouteId: id
        });

        const formik = useFormik({
            enableReinitialize: true,
            initialValues: review,
            onSubmit: (values) => {
                console.log(values)
                fetch(`/reviews`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(values)
                })
                .then(res => {
                    if (res.ok) {
                        res.json().then(data => {
                            setReview(data)
                            history.push(`/routes/${id}`)
                        })
                    } else {
                        res.json().then(error => console.log(error.message))
                    };
            })
            }
        })
        // if (!isLoaded) return <h1>Loading...</h1>;

        return (
            <>
                <div className='new-review-form'>
                    <h2>Add Review</h2>
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
                        <label >Notes:</label>
                        <input type="text"  name="comment" value={formik.values.comment} onChange={formik.handleChange} />
                        <br></br>
                        <button type="submit" value='Save'>Add Review</button>
                        <button type="button" onClick={() => history.goBack()}>Cancel</button>
                    </form>
                </div>
            </>
        );}


export default AddReview