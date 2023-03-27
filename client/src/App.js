import React, { useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Header from "./Header";
import Nav from "./Nav"
import Home from "./Home";
import ClimbingRoutes from "./ClimbingRoutes";
import NewRouteForm from "./NewRouteForm";
import Profile from "./Profile";
import LogIn from "./LogIn";

function App() {
  const [page, setPage] = useState("/")

  return (
    <div className="App">
      <Header />
      <Nav onChangePage={setPage} />
      <Switch>
        <Route path="/crux">
          <Home />
        </Route>
        <Route path="/routes">
          <ClimbingRoutes />
        </Route>
        <Route path="/submit">
          <NewRouteForm />
        </Route>
        <Route path="/profile">
          <Profile />
        </Route>
        <Route path="/log_in">
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