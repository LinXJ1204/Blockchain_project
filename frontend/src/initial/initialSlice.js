import {createSlice } from '@reduxjs/toolkit';
import { store } from '../store';
const { ethereum } = window;


export const user_info = createSlice({
    name: 'user_info',
    initialState: {address:'', userid: 0, user_name:''},
    reducers:{
        set_address: (state, actions) => {
            return {...state, address:actions.payload}
        },
        set_userid: (state, actions) => {
            return {...state, userid:actions.payload}
        },
        set_username: (state, actions) => {
            return {...state, user_name:actions.payload}
        }
    }    
})
