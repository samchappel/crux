import {Link} from 'react-router-dom'

function ClimbingRoutesCard({route}) {
    const {name, style, grade, image, id} = route
    console.log(route)
    
    return (

        <li className="card">
            <div className="image">
            <img src={image} alt={name} />
            </div>
            <div className="details">
                <h2 className="name">{name}</h2>
                <p>{style}</p>
                <p>{grade}</p>
            </div>
        </li>

    )
}

export default ClimbingRoutesCard