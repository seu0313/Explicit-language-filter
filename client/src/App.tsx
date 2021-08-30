import React, { useState } from "react";
import { Switch, Route } from "react-router-dom";
import GlobalThemeProvider from "./styles/GlobalThemeProvider";
import AppLayout from "./components/AppLayout";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";

const App = (): JSX.Element => {
  return (
    <GlobalThemeProvider>
      <AppLayout>
        <AppLayout.Side>
          <Sidebar />
        </AppLayout.Side>
        <AppLayout.Main>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/develop">
              DEVELOP
            </Route>
            <Route component={NotFound} />
          </Switch>
        </AppLayout.Main>
      </AppLayout>
    </GlobalThemeProvider>
  );
};

export default App;
