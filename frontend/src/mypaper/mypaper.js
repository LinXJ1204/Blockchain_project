import { BrowserRouter, Link, Routes, Route } from "react-router-dom";
import Paperlist from './paperlist'
import Notification from '../notification';
import { store } from '../store';
import { useSelector } from 'react-redux';
import { paperlist } from './paperSlice';
import {Apply} from './apply';
import { paper_initial } from './paperlist';



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
                    <a href="#">Dashboard</a>
                  </li>
                  <li><i className='bx bx-chevron-right' ></i></li>
                  <li>
                    <a className="active" href="#">Paper</a>
                  </li>
                </ul>
                </div>
                <a href="#" className="btn-download">
                <i className='bx bxs-cloud-download' ></i>
                <span className="text"><Link to='/paper/apply'>Apply Paper</Link></span>
                </a>
                </div>
            
            <div className="mypaper">
                {<Paperlist paper={paper}/>}
                < Notification />
            </div>
        </div>
    )
}


export default Mypaper;