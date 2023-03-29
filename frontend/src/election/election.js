import { BrowserRouter, Link, Routes, Route, useParams, Outlet } from "react-router-dom";

export function Election(){
    return(
        <div>
            <div className="head-title">
                <div className="left">
                    <h1>Election</h1>
                    <ul className="breadcrumb">
                    <li>
                        <a><Link to='/'>Dashboard</Link></a>
                    </li>
                    <li><i className='bx bx-chevron-right' ></i></li>
                    <li>
                        <a className="active">Election</a>
                    </li>
                    </ul>
                </div>
            </div>
        </div>
    )
}