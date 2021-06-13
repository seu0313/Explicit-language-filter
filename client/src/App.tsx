import React, { useState } from "react";
import GlobalThemeProvider from "styles/GlobalThemeProvider";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Header from "components/modules/Header";
import MainPage from "components/templates/MainPage";
import DetailPage from "components/templates/DetailPage";
import TestPage from "components/templates/TestPage";
import styled from "styled-components";

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 10px;
`

const App: React.FC = (): JSX.Element => {
  const [isUploadClicked, setIsUploadClicked] = useState(false);
  const [isMenuClicked, setIsMenuClicked] = useState(false);

  return (
    <GlobalThemeProvider>
      <Router>
        <Container>
          <Header
            isMenuClicked={isMenuClicked}
            setIsMenuCliecked={setIsMenuClicked}
            isUploadClicked={isUploadClicked}
            setIsUploadClicked={setIsUploadClicked}
          />
        </Container>
        <Switch>
          <Route path="/test" exact component={TestPage} />
          <Route path="/detail/:id" exact component={DetailPage} />
          <Route path="/" exact>
            <MainPage isMenuClicked={isMenuClicked} setIsMenuClicked={setIsMenuClicked} isUploadClicked={isUploadClicked} setIsUploadClicked={setIsUploadClicked}/>
          </Route>

          {/* <Route component={NotFoundPage} /> */}
        </Switch>
      </Router>
    </GlobalThemeProvider>
  );
};

export default App;

