import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

// pages
import { MainPage, NotFoundPage } from "pages";

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact={true} component={MainPage} />
        {/* <Route path="/upload" component={} /> */}
        <Route component={NotFoundPage} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
