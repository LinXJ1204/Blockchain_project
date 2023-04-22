import { BrowserRouter, Link, Routes, Route, useParams } from "react-router-dom";
import Paperlist from './paperlist'
import Notification from '../notification';
import { store } from '../store';
import { useSelector } from 'react-redux';
import { paperlist } from './paperSlice';
import {Apply} from './apply';
import { paper_initial } from './paperlist';
import { Outlet } from "react-router-dom";


function Mypaper(){
    var applymode = useSelector(()=>{return store.getState()['paperlist'].applymode});
    var paper = useSelector(()=> {return store.getState()['paperlist'].paper});
    return(
        <div>
            <div className="head-title">
              <div className="left">
                <h1>Paper</h1>
                <ul className="breadcrumb">
                  <li>
                    <p ><Link to='/'>Dashboard</Link></p>
                  </li>
                  <li><i className='bx bx-chevron-right' ></i></li>
                  <li>
                    <p className="active" ><Link to='/paper'>Paper</Link></p>
                  </li>
                </ul>
              </div>
              <div className="btn-download">
                <i className='bx bxs-cloud-download' ></i>
                <span className="text"><Link to='/paper/apply'>Apply Paper</Link></span>
              </div>
            </div>
            
            <div className="mypaper">
                <Outlet />
            </div>
        </div>
    )
}


export default Mypaper;