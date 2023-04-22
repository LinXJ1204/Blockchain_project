import { BrowserRouter, Link, Routes, Route, useParams } from "react-router-dom";
import {store} from './store';
import { createBrowserRouter, RouterProvider, createRoutesFromElements } from 'react-router-dom';
import './App.css';
import './style.css';
import Mypaper from './mypaper/mypaper'
import User from "./user/user";
import {initial} from './initial/initial'
import Paperlist, {paperlist_loader} from "./mypaper/paperlist";
import { Paperinfo, paperinfo_loader } from "./mypaper/paperinfo";
import { Home } from "./home";
import Apply from "./mypaper/apply";
import { useSelector } from "react-redux";
import { Election } from "./election/election";
import { Review } from "./review/review";
import Reviewpaperlist, { review_paperlist_loader } from "./review/reviewpaperlist";
import Electionlist, {electionlist_loader} from "./election/electoinlist";
import { Newelection } from "./election/newelection";
import { Electioninfo, electioninfo_loader } from "./election/election_info";



function App() {
  var userid = useSelector(()=>{return store.getState()['user_info'].userid})

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
        <Route path="/election" element={<Election />}>
          <Route path="" loader={(params)=>{return electionlist_loader(userid)}} index element={<Electionlist />}></Route>
          <Route path="newelection" element={<Newelection />} />
          <Route path=":electionid" loader={electioninfo_loader} element={<Electioninfo />}></Route>
        </Route>
        <Route path="review" element={<Review />}>
          <Route path="" index loader={()=>{return review_paperlist_loader()}} element={<Reviewpaperlist />}></Route>
        </Route>
      </Route>
    )
  )  
  initial();

/*   const CryptoJS = require("crypto-js");
  

  const plaintext = "E+Fi9KvSgPaUv1ozJPpmMA==";

  var key = "1234"

  key = CryptoJS.SHA256(key);

  console.log(key);

  const iv = CryptoJS.enc.Utf8.parse("This is an IVVV."); // IV (Initialization Vector)

  // Encrypt plaintext
  const ciphertext = CryptoJS.AES.encrypt(plaintext, key, { iv: iv }).toString();

  const rplaintext = CryptoJS.AES.decrypt(plaintext, key, { iv: iv }).toString(CryptoJS.enc.Utf8);

  console.log("Plaintext:", plaintext);
  console.log("Ciphertext:", ciphertext);
  console.log(rplaintext); */


  
  
  return (
      <div className="App">
        <RouterProvider router={router}/>
      </div>
  );
}




export default App;
