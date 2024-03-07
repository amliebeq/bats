import React from 'react'
import { useSelector } from 'react-redux'
import { Applicant } from './Applicant'

export const ApplicantsList = () => {
    const applicants = useSelector(state => state.user.user.applicants)
    const applicantList = applicants.map(applicant => <Applicant key={applicant.id} applicant={applicant} />)
  return (
    <div>{applicantList}</div>
  )
}
