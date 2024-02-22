import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from './components/Layout.jsx';
import Home from './pages/Home.jsx';
import NotFound from './pages/Error.jsx';
import MasterData from './pages/MasterData.jsx';

function App() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Layout />} />
            <Route path="/home" element={<Home />} />
            <Route path="/master_data" element={<MasterData />} />
            <Route path="*" element={<NotFound />} />
        </Routes>
    </BrowserRouter>
  );
}
console.log("Hallo welt");
render(<App />, document.getElementById('root'));