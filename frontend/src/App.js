import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import { Main, NotFound } from './pages'

const App = () => {
  return(
    <BrowserRouter>
      <Switch>
        <Route path='/' exact={true} component={Main}/>
        <Route component={NotFound}/>
      </Switch>
    </BrowserRouter>
  );
}

export default App;