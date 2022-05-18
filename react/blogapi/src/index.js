import React from 'react';
import ReactDOM from 'react-dom/client';
import * as serviceWorker from './serviceWorker';
import './index.css';
import {Route, BrowserRouter, Routes} from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';

const routing = (
<BrowserRouter>
    <React.StrictMode>
    <Header />
    <Routes>
        <Route exact path="/" element={ <App/> } />
    </Routes>
    <Footer />
    </React.StrictMode>
</BrowserRouter>
);
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(routing);

serviceWorker.unregister();