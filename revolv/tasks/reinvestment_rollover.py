import datetime
from django.conf import settings

from revolv.project.models import Project, ProjectMatchingDonors
from revolv.payments.models import ProjectMontlyRepaymentConfig, AdminReinvestment, PaymentType, Payment, SolarSeedFund
from revolv.base.models import RevolvUserProfile
from django.db.models import Sum
from django.db.models import Q
from revolv.tasks.sfdc import send_donation_info

from celery.task import task

import sys
import time
import logging

logger = logging.getLogger("revolv")


@task
def distribute_reinvestment_fund():
    """
    This task is for Automatic reinvestment

    This is how this script do:
    1. Get all project that is eligible for reinvestment:
        (project with monthly_reinvestment_cap >0 and not fully funded)
    2. For each project determine how we'll reinvest
    3. Add AdminReinvestment object with above value
    4. Reinvestment every user's reinvestment amount in project funding proportion.
    """

    today = datetime.datetime.today()
