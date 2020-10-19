import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import { Main, NotFound, Test } from './pages'

const App = () => {
  return(
    <BrowserRouter>
      <Switch>
        <Route path='/' exact={true} component={Main}/>
        <Route path='/test' exact={true} component={Test}/>
        <Route component={NotFound}/>
      </Switch>
    </BrowserRouter>
  );
}

export default App;