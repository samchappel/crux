import React, { useState, useEffect } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav"
import Home from "./Home";
import ClimbingRoutesContainer from "./ClimbingRoutesContainer";
import NewRouteForm from "./NewRouteForm";
import Profile from "./Profile";
import LogIn from "./LogIn";
import SingleRoute from "./SingleRoute"
import RouteEdit from "./RouteEdit"

function App() {
  const [page, setPage] = useState("/")
  const [routes, setRoutes] = useState([])
  const [climber, setClimber] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        fetchClimber()
    },[])

    const fetchClimber = () => {
      fetch('/authorized')
        .then((res) => {
          if (res.ok) {
            setIsLoggedIn(true); 
            return res.json();
          } else {
            setIsLoggedIn(false); 
            setClimber(null);
          }
        })
        .then((data) => {
          setClimber(data);
        });
    };

  useEffect(() => {
    fetch('http://localhost:5555/routes')
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.status}`);
      }
      return response.json();
    })
    .then(setRoutes)
    .catch(error => {
      console.error('Error fetching data:', error);
    });
  }, [])

  return (
    <div className="App">
      <Header />
      <Nav onChangePage={setPage} />
      <Switch>
        <Route path="/featured_routes">
          <Home />
        </Route>
        <Route path="/routes/:id/edit">
          <RouteEdit climber={climber}/>
        </Route>
        <Route path="/routes/:id">
          <SingleRoute climber={climber}/>
        </Route>
        <Route path="/routes">
          <ClimbingRoutesContainer routes={routes} setRoutes={setRoutes} />
        </Route>
        <Route path="/submit">
          <NewRouteForm />
        </Route>
        <Route path="/profile">
          <Profile />
        </Route>
        <Route path="/login">
          <LogIn />
        </Route>
      </Switch>
    </div>
  );
}

function WrappedApp() {
  return (
    <BrowserRouter>
      <App />
    </BrowserRouter>
  )
}

export default WrappedApp;