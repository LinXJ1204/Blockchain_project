import { configureStore, createSlice } from '@reduxjs/toolkit';


export const paperlist = createSlice({
    name: 'paperlist',
    initialState: {paper:[], applymode:false},
    reducers:{
        getpaper: (state, actions) =>{
            return {...state, paper:actions.payload};
        },
        applymodetoggle: (state) => {
            if(state.applymode){
                return {...state, applymode:false};
            }else{
                return {...state, applymode:true};
            }
            
        }
    }
})

