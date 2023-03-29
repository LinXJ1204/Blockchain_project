import { BrowserRouter, Link, Routes, Route, useParams } from "react-router-dom";
import {store} from './store';
import { createBrowserRouter, RouterProvider, createRoutesFromElements } from 'react-router-dom';
import './App.css';
import './style.css';
import Mypaper from './mypaper/mypaper'
import User from "./user/user";
import { ethers } from "https://cdnjs.cloudflare.com/ajax/libs/ethers/6.1.0/ethers.min.js";
import axios from 'axios';
import {initial} from './initial/initial'
import Paperlist, {paperlist_loader} from "./mypaper/paperlist";
import { Paperinfo } from "./mypaper/paperinfo";
import { paperinfo_loader } from "./mypaper/paperinfo";
import { NavLink } from "react-router-dom";
import { Home } from "./home";
import Apply from "./mypaper/apply";
import { useSelector } from "react-redux";
import { Election } from "./election/election";
import { Review } from "./review/review";

const { ethereum } = window;

function App() {
  var userid = useSelector(()=>{return store.getState()['user_info'].userid})
  async function loader({params}){
    return params.paperid;
    }
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path="/" element={<Home/>}>
        <Route path="paper"  element={<Mypaper />} >
          <Route path="" index loader={(params)=>{return paperlist_loader(userid)}} element={<Paperlist />} />
          <Route path="apply" element={<Apply />} />
          <Route path=":paperid" loader={paperinfo_loader} element={<Paperinfo />} />
        </Route>
        <Route path="/user" element={<User/>} />
        <Route index element={<User/>} />
        <Route path="/election" element={<Election />}></Route>
        <Route path="review" element={<Review />}></Route>
      </Route>
    )
  )  
  initial();
  return (
      <div className="App">
        <RouterProvider router={router}/>
      </div>
  );
}




export default App;
