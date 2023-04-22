import { BrowserRouter, Link, Routes, Route, useParams, Outlet } from "react-router-dom";

export function Election(){
    return(
        <div>
            <div className="head-title">
                <div className="left">
                    <h1>Election</h1>
                    <ul className="breadcrumb">
                    <li>
                        <p><Link to='/'>Dashboard</Link></p>
                    </li>
                    <li><i className='bx bx-chevron-right' ></i></li>
                    <li>
                        <p className="active">Election</p>
                    </li>
                    </ul>
                </div>
                <div className="btn-download">
                    <i className='bx bxs-cloud-download' ></i>
                    <span className="text"><Link to='/election/newelection'>New election</Link></span>
                </div>
                
            </div >
            <div className="mypaper">
                <Outlet />
            </div>
        </div>
    )
}