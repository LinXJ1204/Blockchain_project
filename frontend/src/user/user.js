import Notification from '../notification';
import User_info from './user_info';


function User(){
    return(
        <div>
            <div className="head-title">
              <div className="left">
                <h1>Account</h1>
                <ul className="breadcrumb">
                  <li>
                    <a href="#">Dashboard</a>
                  </li>
                  <li><i className='bx bx-chevron-right' ></i></li>
                  <li>
                    <a className="active" href="#">Account</a>
                  </li>
                </ul>
              </div>
                <a href="#" className="btn-download">
                <i className='bx bxs-cloud-download' ></i>
                <span className="text">Edit</span>
                </a>
            </div>
            
            <div className="mypaper">
                <User_info />

            < Notification />
          </div>
        </div>
    )
}


export default User;