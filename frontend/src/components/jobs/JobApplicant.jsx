import React from 'react'
import { Link } from 'react-router-dom'

export const JobApplicant = ({ applicant }) => {

  return (
    <div>
        <Link to={`/applicants/${applicant.id}`}>{applicant.first_name}</Link>
    </div>
  )
}
