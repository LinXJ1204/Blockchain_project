import { Link, useLoaderData } from "react-router-dom";

export async function electionlist_loader(userid){
    const res = await fetch("http://127.0.0.1:5000/election/myelection", {
      method: "post",
      headers: {"Content-Type": "application/json"}, 
      body: JSON.stringify({user_id: userid})
    })
    return res.json()
  }

function Electionlist(){
    var electionlist = useLoaderData().electionlist;
    console.log(electionlist);
    return(
        <div className="paperlist default_list">
            <table>
                <thead>
                <tr>
                    <th>Title</th>
                    <th>invoker</th>
                    <th>Status</th>
                </tr>
                </thead>
                <tbody>
                {electionlist.map((item)=>(
                        <tr key={item.title}>
                            <td>
                            <Link to= {'/election/' + item.election_id}>{item.title}</Link>
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




export default Electionlist;