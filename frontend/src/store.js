import React, { useEffect, useRef, useState} from "react";
import {useSelector, useDispatch, Provider} from "react-redux";
import { configureStore, createSlice } from '@reduxjs/toolkit';
import { paperlist } from "./mypaper/paperSlice";
import { user_info } from "./initial/initialSlice";


export const store = configureStore({
    reducer:{
       paperlist: paperlist.reducer,
       user_info: user_info.reducer,
    
    }
});

