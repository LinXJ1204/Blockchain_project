import { BrowserRouter, Link, Routes, Route } from "react-router-dom";
import {store} from './store';
import './App.css';
import './style.css';
import Mypaper from './mypaper/mypaper'
import User from "./user/user";
import { ethers } from "https://cdnjs.cloudflare.com/ajax/libs/ethers/6.1.0/ethers.min.js";
import axios from 'axios';
import {initial} from './initial/initial'
import { paper_initial } from "./mypaper/paperlist";
import Paperapply from "./mypaper/paperapply";

const { ethereum } = window;



function App() {
  initial();
  return (
    <BrowserRouter>
      <div className="App">
        <section id="sidebar">
          <a href="#" className="brand">
            <i className='bx bxs-smile'></i>
            <span className="text">Journal</span>
          </a>
          <ul className="side-menu top">
            <li>
              <a href="#">
                <i className='bx bxs-doughnut-chart' ></i>
                <span className="text"><Link to="/user">User</Link></span>
              </a>
            </li>
            <li className="active">
              <a href="#">
                <i className='bx bxs-dashboard' ></i>
                <span className="text" onClick={paper_initial}><Link to='/paper'>Paper</Link></span>
              </a>
            </li>
            <li>
              <a href="#">
                <i className='bx bxs-shopping-bag-alt' ></i>
                <span className="text"><Link to='/review'>Review</Link></span>
              </a>
            </li>
            <li>
              <a href="#">
                <i className='bx bxs-doughnut-chart' ></i>
                <span className="text"><Link to='/election'>Election</Link></span>
              </a>
            </li>
          </ul>
          <ul className="side-menu">

            <li>
              <a href="#" className="logout">
                <i className='bx bxs-log-out-circle' ></i>
                <span className="text">Logout</span>
              </a>
            </li>
          </ul>
        </section>



        <section id="content">
          <nav>
            <i className='bx bx-menu' ></i>
            <form action="#">
              <div className="form-input">
                <input type="search" placeholder="Search..."/>
                <button type="submit" className="search-btn"><i className='bx bx-search' ></i></button>
              </div>
            </form>
            <input type="checkbox" id="switch-mode" hidden/>
          </nav>

          <main>
          <Routes>
            <Route path="/paper" element={<Mypaper />} />
            <Route path="/paper/apply" element={<Paperapply />} />
            <Route path="/user" element={<User/>} />
            <Route path="/" element={<User/>} />
          </Routes>
          
          </main>
        </section>
        

        <script src="script.js"></script>

      </div>
    </BrowserRouter>
  );
}




export default App;
