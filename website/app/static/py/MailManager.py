#################################################################
#################################################################
############### Mail Manager API ###############################
#################################################################
#################################################################
##### Author: Denis Torre
##### Affiliation: Ma'ayan Laboratory,
##### Icahn School of Medicine at Mount Sinai

#################################################################
#################################################################
############### 1. Library Configuration ########################
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. Python modules #####
import os
from flask_mail import Message

#############################################
########## 2. Variables
#############################################

#################################################################
#################################################################
############### 1. Send Mail ####################################
#################################################################
#################################################################

#############################################
########## 1. Merge counts
#############################################

def sendMail(id, content, error_type, app, mail):
    
    # Prepare subject
    subject = 'Internal Server Error #{}' if error_type == 'server' else 'Notebook Generation Error #{}'

    # Send mail
    with app.app_context():
        msg = Message(subject=subject.format(id),
                        sender=os.environ['MAIL_USERNAME'],
                        recipients=[os.environ['MAIL_RECIPIENT']],
                        body=content)
        mail.send(msg)
