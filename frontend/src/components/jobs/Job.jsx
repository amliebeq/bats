import React from 'react'

export const Job = ({ job }) => {
  
const jobInfo = 
<ul>
  <h3>{job.title}</h3>
  <p>{job.location}</p>
  <p>{job.pay_rate}</p>
  {job.remote === true ? <p>Remote</p> : <p>In person</p>}
  <p>{job.description}</p>
</ul>

  return (
    <div>
      {jobInfo}
    </div>
  )
}
