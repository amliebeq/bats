import React from 'react'
import { useSelector } from 'react-redux'
import { Job } from './Job'

export const JobsList = () => {
    const jobs = useSelector(state => state.user.user.jobs)

    const jobsList = jobs.map(job => <Job job={job} key={job.id} />)

  return (
    <div>
        {jobsList}
    </div>
  )
}
