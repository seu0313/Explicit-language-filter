import React from "react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import TestPage from "components/templates/TestPage";

const App: React.FC = (): JSX.Element => {
  return (
    <GlobalThemeProvider>
      <Router>
        <Switch>
          <Route exact path="/" component={TestPage} />
          {/* <Route exact path="/" component={} /> */}
          {/* <Route path="/upload" component={} /> */}
          {/* <Route component={NotFoundPage} /> */}
        </Switch>
      </Router>
    </GlobalThemeProvider>
  );
};

export default App;
