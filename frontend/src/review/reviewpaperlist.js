import axios from 'axios';
import { useSelector } from "react-redux";
import { Link, useLoaderData } from "react-router-dom";

export async function review_paperlist_loader(field=""){
    const res = await fetch("http://127.0.0.1:5000/review/get_paper_review", {
      method: "post",
      headers: {"Content-Type": "application/json"}, 
      body: JSON.stringify({field: field})
    })
    return res.json()
  }

function Reviewpaperlist(){
    var paper = useLoaderData();
    console.log(paper)
    return(
        <div className="paperlist default_list">
            <div className="head">

            </div>
            <table>
                <thead>
                <tr>
                    <th>Title</th>
                    <th>Date Apply</th>
                </tr>
                </thead>
                <tbody>
                {paper.map((item)=>(
                        <tr key={item.paper_id}>
                            <td>
                            <Link to= {'/paper/' + item.paper_id}>{item.paper_title}</Link>
                            </td>
                            <td></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}




export default Reviewpaperlist;