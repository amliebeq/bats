import React from 'react'
import { useSelector } from 'react-redux'
import { Link, useParams } from 'react-router-dom'

export const JobDetail = () => {
    const { id } = useParams()
    const user = useSelector(state => state.user.user)
    const job = user.jobs.find(job => job.id == id)
    const job_applicants = user.applicants.filter(applicant => applicant.job_id == id)
    
  return (
    <div>
      <h1>{job.title}</h1>
      <p>{job.description}</p>
      <p>{job.location}</p>
      {job.remote === true ? <p>Remote</p> : <p>In person</p>}
    </div>
  )
}
