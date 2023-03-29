
import { Outlet, Link } from "react-router-dom"
import { paper_initial } from "./mypaper/paperlist"


export function Home(){
    return(
        <div className="home">
        <section id="sidebar">
          <div href="#" className="brand">
            <i className='bx bxs-smile'></i>
            <span className="text">Journal</span>
          </div>
          <ul className="side-menu top">
            <li>
              <div href="#">
                <i className='bx bxs-doughnut-chart' ></i>
                <span className="text"><Link to="/user">User</Link></span>
              </div>
            </li>
            <li className="active">
              <div href="#">
                <i className='bx bxs-dashboard' ></i>
                <span className="text"><Link to='/paper'>Paper</Link></span>
              </div>
            </li>
            <li>
              <div href="#">
                <i className='bx bxs-shopping-bag-alt' ></i>
                <span className="text"><Link to='/review'>Review</Link></span>
              </div>
            </li>
            <li>
              <div href="#">
                <i className='bx bxs-doughnut-chart' ></i>
                <span className="text"><Link to='/election'>Election</Link></span>
              </div>
            </li>
          </ul>
          <ul className="side-menu">

            <li>
              <div href="#" className="logout">
                <i className='bx bxs-log-out-circle' ></i>
                <span className="text">Logout</span>
              </div>
            </li>
          </ul>
        </section>



        <section id="content">
          <nav>
            <i className='bx bx-menu' ></i>
            <form action="#">
              <div className="form-input">
                <input type="search" placeholder="Search..."/>
                <button type="submit" className="search-btn"><i className='bx bx-search' ></i></button>
              </div>
            </form>
            <input type="checkbox" id="switch-mode" hidden/>
          </nav>

          <main>
        <Outlet />
          </main>
        </section>
        

        <script src="script.js"></script>

      </div>
    )
}