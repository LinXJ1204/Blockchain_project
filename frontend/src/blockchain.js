import axios from "axios";
import { ethers } from "https://cdnjs.cloudflare.com/ajax/libs/ethers/6.1.0/ethers.min.js";
import { store } from "./store";

let abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"end_time","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Vote_end","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"start_time","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Vote_start","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Voter_set","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"voter","type":"address"},{"indexed":false,"internalType":"string","name":"ballot","type":"string"},{"indexed":false,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Voting_complete","type":"event"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"get_ballot","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"},{"internalType":"uint256","name":"proposal_duration","type":"uint256"}],"name":"new_proposal","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"candidates","type":"address[]"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_candidates","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_duration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"voters","type":"address[]"},{"internalType":"uint256[]","name":"user_id","type":"uint256[]"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_voters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ballot","type":"string"},{"internalType":"uint256","name":"proposal_id","type":"uint256"},{"internalType":"uint256","name":"voter_id","type":"uint256"}],"name":"voting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"voting_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"voting_start","outputs":[],"stateMutability":"nonpayable","type":"function"}];
let smartcontract_address = '0x10390e9988D1fc4e19Fe1cC0b6927e62702F9b4c';
let signer = null;
let provider;

async function sc_initial(){
        
        if (window.ethereum == null) {
            console.log("MetaMask not installed; using read-only defaults")
            provider = ethers.getDefaultProvider()
        } else {
            provider = new ethers.BrowserProvider(window.ethereum)
            signer = await provider.getSigner();
            console.log(signer);
            return signer;
        }}



export default sc_initial;

