import { createSlice } from "@reduxjs/toolkit";

const slice = createSlice({
    name: 'user',
    initialState: {
        user: null,
        hasAccount: true
    },
    reducers: {
        toggleAccount: state => {
            state.hasAccount = !state.hasAccount
        },
        userAdded: (state, action) => {
            state.user = action.payload
        }
    }
})

export const { toggleAccount, userAdded } = slice.actions

export default slice.reducer