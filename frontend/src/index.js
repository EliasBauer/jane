import React, { Component } from 'react';
import { render } from 'react-dom';

export default function App() {
  return (
    <div>
      <h1>Hello, world!</h1>
    </div>
  );
}

render(<App />, document.getElementById('root'));