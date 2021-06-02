import React from "react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

const App: React.FC = () => {
  return (
    <GlobalThemeProvider>
      <Router>
        <Switch>
          {/* <Route path="/" exact={true} component={MainPage} /> */}
          {/* <Route path="/upload" component={} /> */}
          {/* <Route component={NotFoundPage} /> */}
        </Switch>
      </Router>
    </GlobalThemeProvider>
  );
};

export default App;
