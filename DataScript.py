import os

print ("Converting SFDX to Metadata")

datapull=os.system('git pull origin master')
print ("####Data Pull Completed####")
if(datapull==0):
    os.system('sfdx force:source:convert -d mdapioutput/')
    deployData=os.system('ant deployUnpackaged')
    if(deployData==0):
        print ("Deployment success")
    else:
        print ("Deployment Failed")
    

