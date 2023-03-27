import { store } from "../store";
import { paper_apply } from "../blockchain";
import axios from 'axios';
import sc_initial from '../blockchain';
import { ethers } from "https://cdnjs.cloudflare.com/ajax/libs/ethers/6.1.0/ethers.min.js";
import { data } from "jquery";





function set_proposal(proposal_id){
    return  sc_initial().then((signer)=>{
                let smartcontract_address = '0x10390e9988D1fc4e19Fe1cC0b6927e62702F9b4c';
                let abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"end_time","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Vote_end","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"start_time","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Vote_start","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Voter_set","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"string","name":"ballot","type":"string"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Voting_complete","type":"event"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"get_ballot","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"},{"internalType":"uint256","name":"proposal_duration","type":"uint256"}],"name":"new_proposal","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"candidates","type":"address[]"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_candidates","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_duration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"voters","type":"address[]"},{"internalType":"uint256[]","name":"user_id","type":"uint256[]"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_voters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ballot","type":"string"},{"internalType":"uint256","name":"proposal_id","type":"uint256"},{"internalType":"uint256","name":"voter_id","type":"uint256"}],"name":"voting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"voting_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"voting_start","outputs":[],"stateMutability":"nonpayable","type":"function"}];
                const contract = new ethers.Contract(smartcontract_address, abi, signer);
                contract.new_proposal(proposal_id, 23123123).then(()=>{window.alert('Apply ok')})
            })
}

function applydb(title){
    var user_id = store.getState().user_info.userid;
   axios({
    method: 'post',
    url: "http://127.0.0.1:5000/review/paper_data",
    data: ({user_id: user_id, title:title})
  }).then(response => {
    set_proposal(response.data.data)
})
}

export function Apply(){

    return(
        <div className="apply ">
            <div className="head">
                <h3>Apply</h3>
                <i className='bx bx-search' ></i>
                <i className='bx bx-filter' ></i>
            </div>
            <div>
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
                            <p>Paper Title</p>
                            </td>
                            <td><input type="text" name="papertitle" id="papertitle"/></td>
                        </tr>
                        <tr>
                            <td>
                            <p id='apply_result'></p>
                            </td>
                            <td></td>
                        </tr>
                        </tbody>
                    </table>
                    <input className= 'applypaperbuttom' type="submit" value="Apply" onClick={()=>{
                        applydb(document.getElementById('papertitle').value)}}/>
                        
            </div>
        </div>
    )
}


export default Apply;