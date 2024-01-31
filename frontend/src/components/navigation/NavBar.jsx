import React from 'react'
import { Link, Navigate } from 'react-router-dom'

export const NavBar = () => {
  return (
    <div>
        <nav>
            <Link to={'/'}>Home</Link>
            <Link to={'jobs'}>Jobs</Link>
        </nav>        
    </div>
  )
}
