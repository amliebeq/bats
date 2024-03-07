import React from 'react'
import { useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'

export const JobDetail = () => {
    const { id } = useParams()
    const jobs = useSelector(state => state.user.user.jobs)
    const job = jobs.find(job => job.id == id)
    console.log(job)
  return (
    <div>JobDetail</div>
  )
}
