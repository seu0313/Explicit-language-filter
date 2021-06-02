import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

// pages
import {
  HomePage,
  NotFoundPage,
  VideoUploadPage,
  LoginPage,
  RegisterPage,
} from "./pages";

// components
import { NavBarAdvanced } from "./components/NavBar";

const App = () => {
  return (
    <BrowserRouter>
      <NavBarAdvanced />
      <Switch>
        <Route path="/" exact={true} component={HomePage} />

        {/* Auth */}
        <Route path="/login" component={LoginPage} />
        <Route path="/signup" component={RegisterPage} />
        {/* <Route path='/profile' component={RegisterPage} />
        <Route path='/account' component={RegisterPage} /> */}

        {/* Video function */}
        <Route path="/upload" component={VideoUploadPage} />
        {/* <Route path='/video/mypage' component={} /> */}

        {/* 404 Page */}
        <Route component={NotFoundPage} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
