import React from "react";
import { Switch, Route } from "react-router-dom";
import GlobalThemeProvider from "./styles/GlobalThemeProvider";
import AppLayout from "./components/AppLayout";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import TextFilter from "./pages/TextFilter";
import AudioFilter from "./pages/AudioFilter";
import VideoFilter from "./pages/VideoFilter";

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
            <Route exact path="/text" component={TextFilter} />
            <Route exact path="/audio" component={AudioFilter} />
            <Route exact path="/video" component={VideoFilter} />
            <Route component={NotFound} />
          </Switch>
        </AppLayout.Main>
      </AppLayout>
    </GlobalThemeProvider>
  );
};

export default App;
