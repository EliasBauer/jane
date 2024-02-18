import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Layout from './components/Layout.jsx';
import Home from './pages/Home.jsx';
import NotFound from './pages/NotFound.jsx';

function App() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
            </Route>
            <Route path="*" element={<NotFound />} />
        </Routes>
    </BrowserRouter>
  );
}

render(<App />, document.getElementById('root'));