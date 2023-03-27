import { store } from "../store";
import axios from 'axios';
import { paperlist } from "./paperSlice";
import { useSelector } from "react-redux";

export function paper_initial(){
    
   var user_id = store.getState().user_info.userid;
   axios({
    method: 'post',
    url: "http://127.0.0.1:5000/user/get_mypaper",
    data: ({user_id: user_id})
  }).then(response => {
    store.dispatch(paperlist.actions.getpaper(response.data.data))
    console.log('OK');
})
}

function Paperlist(props){
    return(
        <div className="paperlist default_list">
            <div className="head">
                <h3>Paper List</h3>
                <i className='bx bx-search' ></i>
                <i className='bx bx-filter' ></i>
            </div>
            <table>
                <thead>
                <tr>
                    <th>Title</th>
                    <th>Date Apply</th>
                    <th>Status</th>
                </tr>
                </thead>
                <tbody>
                {props.paper.map((item)=>(
                        <tr key={item.title}>
                            <td>
                            <p>{item.title}</p>
                            </td>
                            <td></td>
                            <td><span className="status completed">{item.status}</span></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}




export default Paperlist;