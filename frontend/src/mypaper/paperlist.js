import { store } from "../store";
import axios from 'axios';
import { paperlist } from "./paperSlice";
import { useSelector } from "react-redux";
import { Link, useLoaderData } from "react-router-dom";

export async function paperlist_loader(userid){
    const res = await fetch("http://127.0.0.1:5000/user/get_mypaper", {
      method: "post",
      headers: {"Content-Type": "application/json"}, 
      body: JSON.stringify({user_id: userid})
    })
    return res.json()
  }

function Paperlist(){
    var paper = useLoaderData().data;
    return(
        <div className="paperlist default_list">
            <div className="head">
                <h3>Your Paper</h3>
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
                {paper.map((item)=>(
                        <tr key={item.paper_id}>
                            <td>
                            <Link to= {'/paper/' + item.paper_id}>{item.title}</Link>
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