import { BrowserRouter, Link, Routes, Route, useParams, Outlet } from "react-router-dom";
import Reviewpaperlist from "./reviewpaperlist";
import { review_paperlist_loader } from "./reviewpaperlist";

export function Review(){

    return(
        <div>
            <div className="head-title">
                <div className="left">
                    <h1>Review</h1>
                    <ul className="breadcrumb">
                    <li>
                        <p><Link to='/'>Dashboard</Link></p>
                    </li>
                    <li><i className='bx bx-chevron-right' ></i></li>
                    <li>
                        <p className="active" >Review</p>
                    </li>
                    </ul>
                </div>
            </div>
            <div className="mypaper">
                <Outlet />
            </div>
        </div>
    )
}