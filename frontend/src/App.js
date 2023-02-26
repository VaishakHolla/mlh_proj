import logo from './logo.svg';
import './App.css';
//theme
import "primereact/resources/themes/lara-dark-blue/theme.css";
//core
import "primereact/resources/primereact.min.css";
//icons
import "primeicons/primeicons.css";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import ErrorPage from './pages/error-page';
import Navigation from './components/navigation';
import Home from './pages/home';
import Visualization from './pages/visualization';
import Analysis from './pages/analysis';
import Sources from './pages/sources';
import About from './pages/about';
import Contact from './pages/contact';

function App() {
  return (
    <div className="App">
      <Navigation/>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About/>}/>
          <Route path="/contact" element={<Contact/>}/>
          <Route path="/viz" element={<Visualization/>}/>
          <Route path="/analysis" element={<Analysis/>}/>
          <Route path="/sources" element={<Sources/>}/>

          <Route exact={true} path="*" element={<ErrorPage />} />
          </Routes>
          </BrowserRouter>
    </div>
  );
}

export default App;
