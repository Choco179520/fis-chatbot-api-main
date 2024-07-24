from static.documents.payments.payments import *
from static.documents.undergraduate_reentry.undergraduate_reentry_process import *
from static.documents.extra.extra import *
from static.documents.scholarships.scholarship_types import *
from static.documents.socioeconomic_data.socioeconomic_data_update import *
from static.documents.enrollment.enrollment_types import *
from static.documents.enrollment.regular_enrollment import *
from static.documents.enrollment.special_enrollment import *
from static.documents.enrollment.extraordinary_enrollment import *
from static.documents.default_answers.thanks import *
from static.documents.default_answers.greetings import *

documents = [
    undergraduate_reentry_process,
    socioeconomic_data_to_undergraduate_reentry_process,
    scholarship_types,
    cultural_merit_scholarships,
    academic_excellence_scholarships,
    economic_vulnerability_scholarships,
    socioeconomic_data_update,
    enrollment_types,
    regular_enrollment,
    regular_enrollment_requirements,
    regular_enrollment_process,
    assisted_regular_enrollment,
    extraordinary_enrollment,
    special_enrollment,
    special_enrollment_process,
    payment_selection,
    payment_dates_delays,
    policy_surcharges_delay,
    economic_difficulties_quotas,
    academic_calendar_start_classes,
    voluntary_contributions,
    loss_of_gratuity,
    voluntary_retirement_subjects,
    withdrawal_subjects_fortuitous_event,
    extemporaneous_retirement_subjects,
    concession_third_registration,
    billing_payments_saew,
    non_credit_subjects,
    pre_professional_practices,
    registrations_other_units,
    curriculum_meshes,
    academic_honesty,
    enrollment_restrictions,
    greetings,
    thanks,
    english_acomplishment,
    admission_process,
]
