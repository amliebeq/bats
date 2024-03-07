import React from 'react'
import { useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { JobApplicant } from './JobApplicant'

export const JobDetail = () => {
    const { id } = useParams()
    const user = useSelector(state => state.user.user)
    const job = user.jobs.find(job => job.id == id)
    const applicants = user.applicants
    const job_applicants = applicants.map(applicant => <JobApplicant key={applicant.id} applicant={applicant}/>)


    
  return (
    <div>
      <h1>{job.title}</h1>
      <p>{job.description}</p>
      <p>{job.location}</p>
      {job.remote === true ? <p>Remote</p> : <p>In person</p>}
      {job_applicants}
    </div>
  )
}
