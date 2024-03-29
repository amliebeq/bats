import React from 'react'
import { Link } from 'react-router-dom'

export const Job = ({ job }) => {

  return (
    <div>
      <Link to={`/jobs/${job.id}`}>{job.title}</Link>
      <p>{job.location}</p>
      <p>{job.pay_rate}</p>
      {job.remote === true ? <p>Remote</p> : <p>In person</p>}
      <p>{job.description}</p>
    </div>
  )
}
