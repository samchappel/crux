import {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { useFormik } from "formik";
import { useHistory } from 'react-router-dom';

function RouteEdit() { //{climber} add
    const history = useHistory();
    const {id} = useParams();  
    const [route, setRoute] = useState({
        name: '',
        style: '',
        grade: '',
        image: '',
        //locationPlace: ''
        });
        const [isLoaded, setIsLoaded] = useState(true);
        useEffect(()=>{
            console.log(id)
            fetch(`http://localhost:5555/routes/${id}`)
            .then(res=>res.json())
            .then((data) => {
                setRoute(data);
                setIsLoaded(true);
            })
        }, [id])

    const formik = useFormik({
        enableReinitialize: true,
        initialValues: route,
        onSubmit: (values) => {
            fetch(`/routes/${id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        setRoute(data)
                        history.push('/routes')
                    })
                } else {
                    res.json().then(error => console.log(error.message))
                };
        })
        }
    })


    if (!isLoaded) return <h1>Loading...</h1>;
    // if ((climber&&climber.is_admin === false) || (!climber)) {
    //     return <h1>Cannot edit this Route</h1>
    // } else {
        return (
            <>
                <div className='new-route-form'>
                    <h2>Edit Route</h2>
                    <form onSubmit={formik.handleSubmit} >
                        <label >Name:</label>
                        <input type="text"  name="name" value={formik.values.name} onChange={formik.handleChange} />
                        <br></br>
                        <label >Style:</label>
                        <input type="text"  name="style" value={formik.values.style} onChange={formik.handleChange} />
                        <br></br>
                        <label >Grade:</label>
                        <input type="text"  name="grade" value={formik.values.grade} onChange={formik.handleChange} />
                        <br></br>
                        {/* <label >Location ID:</label>
                        <input type="text"  name="location_id" value={formik.values.location_id} onChange={formik.handleChange} />
                        <br></br> */}
                        <label >Image:</label>
                        <input type="text"  name="image" value={formik.values.image} onChange={formik.handleChange} />
                        <br></br>
                        <button type="submit" value='Save'>Update</button>
                        <button type="button" onClick={() => history.goBack()}>Cancel</button>
                    </form>
                </div>
            </>
        );
    }


export default RouteEdit