import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import App from './App';

// Import the octofitapp-small logo
import logo from '../public/octofitapp-small.png';

// Add the favicon
const link = document.createElement('link');
link.rel = 'icon';
link.href = '../public/favicon.ico';
document.head.appendChild(link);

ReactDOM.render(
  <React.StrictMode>
    <div className="logo">
      <img src={logo} alt="OctoFit Logo" />
      <App />
    </div>
  </React.StrictMode>,
  document.getElementById('root')
);
