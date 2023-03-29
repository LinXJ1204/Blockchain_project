import { BrowserRouter, Link, Routes, Route, useParams, useLoaderData } from "react-router-dom";
import Notification from "../notification";
import Paperlist from "./paperlist";
import { useSelector } from 'react-redux';
import { store } from "../store";
import axios from 'axios';

export async function paperinfo_loader({params}){
    const res = await fetch("http://127.0.0.1:5000/review/get_paper_info", {
      method: "post",
      headers: {"Content-Type": "application/json"}, 
      body: JSON.stringify({paper_id: params.paperid})
    })
    return res.json()
  }

  

export function Paperinfo(){
    var paper_info = useLoaderData();
    return (
        <div className="paperlist default_list">
            <div className="head">
                <h3>{paper_info.title}</h3>
                <i className='bx bx-search' ></i>
                <i className='bx bx-filter' ></i>
            </div>
            <table>
                <thead>
                <tr>
                    <th></th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Title</td>
                    <td style={{textAlign:'left'}}>{paper_info.title}</td>
                    <td></td>
                </tr>
                </tbody>
            </table>
        </div>
    )
}