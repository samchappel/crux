import React from "react";
import ClimbingRoutesCard from './ClimbingRoutesCard'

function ClimbingRoutesContainer({routes, setRoutes}) {

    const routeCards = routes.map(route => <ClimbingRoutesCard key={route.id} route={route} setRoutes={setRoutes}/>)

    return (
        <div>
            <ul className="cards">{routeCards}</ul>
        </div>
    )
}

export default ClimbingRoutesContainer