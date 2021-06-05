import React from "react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import MainPage from "components/templates/MainPage";
import TestPage from "components/templates/TestPage";

const App: React.FC = (): JSX.Element => {
  return (
    <GlobalThemeProvider>
      <Router>
        <Switch>
          <Route exact path="/test" component={TestPage} />
          <Route exact path="/" component={MainPage} />
          {/* <Route path="/upload" component={} /> */}
          {/* <Route component={NotFoundPage} /> */}
        </Switch>
      </Router>
    </GlobalThemeProvider>
  );
};

export default App;
