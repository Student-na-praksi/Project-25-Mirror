import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import './index.css'
import './globals.css'
import AdminPage from './AdminPage/AdminPage.tsx'
import LandingPage from './LandingPage/LandingPage.tsx'
import UserPage from './UserPage/UserPage.tsx'


ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage/>}/>
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/user" element={<UserPage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
