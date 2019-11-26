from celery.task import task
from simple_salesforce import Salesforce

from django.conf import settings
from django.utils import log

logger = log.getLogger(__name__)

INTERVAL = 10 * 60  # 10 minutes
MAX_RETRIES = 100


class SFDCException(Exception):
    pass


#@task
def send_signup_info(name, email, address=''):
    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'donorName': name, 'email': email, 'donorAddress': ''}
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )
        logger.info('send sign-up to SFDC with data: %s', payload)
        res = sf.apexecute(settings.SFDC_REVOLV_SIGNUP, method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC sign-up: sucess.')
    except Exception as e:
        logger.error('SFDC sign-up: ERROR for name: %s and data: %s, res: %s', name, payload, res, exc_info=True)
        #send_signup_info.retry(args=[name, email, address], countdown=INTERVAL, exc=e, max_retries=MAX_RETRIES)

#@task
def send_nonprofit_info(firstnamedt, lastnamedt, emaildt, orgnamedt, orgaddressdt, orgstatedt, zipcodedt, websitedt, affiliatedt, nonprofitdt, nonprofitbuildt):

    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'lastName': 'nonprofitlead', 'company': 'leadNonprpfit', 'email': 'nonprofitformdata4@re-volv.org' }
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )

        sf.Lead.create({'FirstName':firstnamedt, 'LastName':lastnamedt, 'Email': emaildt, 'Company': orgnamedt, 'Street': orgaddressdt, 'State': orgstatedt, 'Country': 'United States',  'PostalCode': zipcodedt, 'Website' : websitedt, 'Title': affiliatedt, 'Certified_501c3_nonprofit__c' : nonprofitdt, 'Owns_Building__c': nonprofitbuildt })
        
        logger.info('send sign-up to SFDC with data: %s', payload)
        #res = sf.apexecute('lead', method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC sign-up: sucess.')
    except Exception as e:
        logger.error('SFDC sign-up: ERROR for name: %s and data: %s, res: %s', emaildt, payload, res, exc_info=True)

#@task
def send_volunteer_info(firstnamedt, lastnamedt, emaildt, zipcodedt, colstudentdt, headsourcedt, orgnamedt, orgaddressdt, websitedt, affiliatedt):

    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'lastName': 'nonprofitlead', 'company': 'leadNonprpfit', 'email': 'nonprofitformdata4@re-volv.org' }
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )

        if orgnamedt == '':
            orgnamedt = 'Solar Ambassador/Champion'
        elif orgnamedt == None:
            orgnamedt = 'Solar Ambassador/Champion'

        if colstudentdt == 'Yes':
            colstudentdt = 'College Fellow'
        elif colstudentdt == 'No':
            colstudentdt = 'Community Champion'

        sf.Lead.create({'FirstName':firstnamedt, 'LastName':lastnamedt, 'Email': emaildt, 'PostalCode': zipcodedt, 'Company': orgnamedt, 'Volunteer_Type__c': colstudentdt, 'Referral_Type__c': headsourcedt, 'Street': orgaddressdt, 'Website' : websitedt, 'Title': affiliatedt})
        
        logger.info('send sign-up to SFDC with data: %s', payload)
        #res = sf.apexecute('lead', method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC sign-up: sucess.')
    except Exception as e:
        logger.error('SFDC sign-up: ERROR for name: %s and data: %s, res: %s', emaildt, payload, res, exc_info=True)

#@task
def send_donation_info(name, amount,email, project, projectmain, postalcode, address=''):
    if not settings.SFDC_ACCOUNT:
        return
    try:
        res = None
        payload = {'donorName': name, 'donorEmail':email, 'projectName': 'Solar Seed Fund', 'donationAmount': amount, 'donorAddress': ''}
        sf = Salesforce(
            username=settings.SFDC_ACCOUNT,
            security_token=settings.SFDC_TOKEN,
            password=settings.SFDC_PASSWORD
        )

        campaigns = ['Purdue University','UC Santa Barbara','UW Milwaukee''American University','UC Santa Cruz','Coastal Carolina University','The Claremont Colleges','USC','Yale University','University of Dayton','University of Oregon','Solar Seed Fund']


        description = 'Donation for ' + project
        # if campaign title is one of the static campaign in the array pass through, else use static Solar Seed Fund for sub campaigns
        if any(project in s for s in campaigns):
            payload = {'donorName': name, 'donorEmail':email, 'projectName': project, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'donorAddress': ''}
        else:
            payload = {'donorName': name, 'donorEmail':email, 'projectName': projectmain, 'donationAmount': amount, 'projectTitle': description, 'postalCode': postalcode, 'donorAddress': ''}

        send_signup_info(name, email, address='')

        logger.info('send donation to SFDC with data: %s', payload)
        res = sf.apexecute(settings.SFDC_REVOLV_DONATION, method='POST', data=payload)
        if res.lower() != 'success':
            raise SFDCException(res)
        logger.info('SFDC donation: success.')
    except Exception as e:
        logger.error('SFDC donation: ERROR for name: %s and data: %s, res: %s', name, payload, res, exc_info=True)
        # send_donation_info.retry(args=[name, amount, project, address], countdown=INTERVAL, exc=e,
        #                          max_retries=MAX_RETRIES)