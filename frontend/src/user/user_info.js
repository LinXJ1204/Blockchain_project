import { useSelector } from "react-redux";
import { store} from "../store";



function User_info(props){
    var userid = useSelector(()=>{return store.getState()['user_info'].userid})
    var useraddress = useSelector(()=>{return store.getState()['user_info'].address})
    var username = useSelector(()=>{return store.getState()['user_info'].user_name})
    return(
        <div className="default_list">
            <div className="head">
                <h3>Hello {username}!</h3>
                <i className='bx bx-search' ></i>
                <i className='bx bx-filter' ></i>
            </div>
            <table>
            <thead>
                <tr>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>
                        <p>Account</p>
                        <p id="account"></p>
                    </td>
                    <td>
                        <p style={{textAlign:'left'}}>{useraddress}</p>
                        <p id="account"></p>
                    </td>
                </tr>
                <tr>
                    <td>
                        <p>Your ID</p>
                        <div id="user_id"></div>
                    </td>
                    <td>
                        <p style={{textAlign:'left'}}>{userid}</p>
                        <div id="user_id"></div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    )
}


export default User_info;