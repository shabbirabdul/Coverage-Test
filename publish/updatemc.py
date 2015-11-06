import subprocess
import mailchimp
from sqlalchemy import Table, MetaData, create_engine
from sqlalchemy.sql import select
import os, sys
import zipfile
from ftplib import FTP

MAILCHIMP_API_KEY = '1ea7497c039210c56d9f6652fb873968-us8'  # USDA Southeast Regional Climate Hub Account
LIST_ID = '6a04cadb00'                                      # Development Testing List
mc = mailchimp.Mailchimp(MAILCHIMP_API_KEY)

def clearAlerts():
    mc.lists.merge_var_set(LIST_ID, 'ALERT', 'No')

def getSubscribers():
    return [member['email'] for member in mc.lists.members(LIST_ID)['data']]
    
def setAlert(email):
    return mc.lists.update_member(LIST_ID, {'email':email}, {'ALERT':'Yes'})

def checkAlertStatus():

    host = 'dev.taccimo.info'
    database = 'serchlights'
                           #dialect+driver://username:password@host:port/database
    engine = create_engine('postgresql+psycopg2://postgres:postgres@{0}:5432/{1}'.format(host, database))

    alertEmails = []
    with engine.connect() as conn:    
        meta = MetaData()
        subscribers = Table('monthly_alert', meta, schema='drought',                  
                            autoload=True, autoload_with=conn)
        s = select([subscribers.c.email])
        result = conn.execute(s)
        for row in result:
            alertEmails.append(row[0])    
    return alertEmails


def updateSubscriberStatus():
    
    clearAlerts()
    alertStatus = checkAlertStatus()
    for subscriber in getSubscribers():
        if subscriber in alertStatus:
            setAlert(subscriber)
            

def downloadMDO(savepath):

    # Download Monthly Drought Outlook from ftp://ftp.cpc.ncep.noaa.gov/GIS/droughtlook/
    # Check security group add 'Custom TCP - Port 21 - 140.90.101.71/32'    
    ftp = FTP('ftp.cpc.ncep.noaa.gov')
    ftp.login()
    ftp.cwd('GIS/droughtlook/') 
    mdolist = [fname for fname in ftp.nlst() 
               if re.match(r'^mdo_polygons_[0-9]{8}.zip', fname)]
    filename = mdolist.sort().pop()
    ftp.retrbinary("RETR " + filename ,open(os.path.join(savepath, filename), 'wb').write)
    ftp.quit()
    return filename

#===============================================================================
# with zipfile.ZipFile(os.path.join(sys.path[1], filename), "r") as z:
#     z.extractall(os.path.join(sys.path[1], filename)[:-4])
#===============================================================================


           
#C:\Program Files\PostgreSQL\9.3\bin\shp2pgsql.exe