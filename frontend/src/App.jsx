import { useEffect } from 'react'
import './App.css'
import { Route, Routes } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { userAdded } from './redux/UserSlice'
import { JobsList } from './components/jobs/JobsList'
import { HomePage } from './components/homePage/HomePage'
import { NavBar } from './components/navigation/NavBar'
import { JobDetail } from './components/jobs/JobDetail'
import { ApplicantsList } from './components/applicants/ApplicantsList'

const App = () => {
  const dispatch = useDispatch()
  const user = useSelector(state => state.user.user)

  useEffect(() => {
    fetch('/api/users/1')
    .then((r) => {
      if (r.ok) {
        r.json().then ((user) => dispatch(userAdded(user)))
      }
    })
  }, [dispatch])

  if (!user) {
    return <></>
  }

  console.log(user)
  return (
    <div>
      <NavBar />
      <Routes>
        <Route exact path='/' element={<HomePage />} />
        <Route exact path='jobs' element={<JobsList />} />
        <Route exact path='applicants' element={<ApplicantsList />} />
        <Route exact path = 'jobs/:id' element={<JobDetail />} />
      </Routes>
    </div>
    
  )
}

export default App     