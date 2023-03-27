import Paperlist from './paperlist'
import Notification from '../notification';
import { store } from '../store';
import { useSelector } from 'react-redux';
import { paperlist } from './paperSlice';
import {Apply} from './apply';
import { paper_initial } from './paperlist';



function Paperapply(){
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
                <a href="#" className="btn-download" onClick={()=>store.dispatch(paperlist.actions.applymodetoggle())}>
                <i className='bx bxs-cloud-download' ></i>
                <span className="text">Apply Paper</span>
                </a>
                </div>
            
            <div className="mypaper">
                {<Apply />}
                < Notification />
            </div>
        </div>
    )
}


export default Paperapply;