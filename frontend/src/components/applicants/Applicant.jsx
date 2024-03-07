import React from 'react'
import { Link } from 'react-router-dom'

export const Applicant = ({ applicant }) => {
    return (
        <div>
            <Link to={`/applicants/${applicant.id}`}>{applicant.first_name} {applicant.last_name}</Link>
            <p>{applicant.email}</p>
            <p>{applicant.phone_number}</p>
            <p>{applicant.recent_job}</p>
        </div>
    )
}
