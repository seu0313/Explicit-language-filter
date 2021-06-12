import React from "react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import MainPage from "components/templates/MainPage";
import DetailPage from "components/templates/DetailPage";
import TestPage from "components/templates/TestPage";

const App: React.FC = (): JSX.Element => {
  return (
    <GlobalThemeProvider>
      <Router>
        <Switch>
          <Route path="/test" exact component={TestPage} />
          <Route path="/detail/:id" exact component={DetailPage} />
          <Route path="/" exact component={MainPage} />

          {/* <Route component={NotFoundPage} /> */}
        </Switch>
      </Router>
    </GlobalThemeProvider>
  );
};

export default App;
