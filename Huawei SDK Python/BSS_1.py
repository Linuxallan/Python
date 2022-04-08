from email import header
from openstack import connection
import sys
import json
from openstack import utils
utils.enable_logging(debug=False,stream=sys.stdout)

import requests

username = "acortes"
password = "huame82gus_"
userDomainId = "605ff9aef384489ab0c518dba4535b5e"
DomainId = "605ff9aef384489ab0c518dba4535b5e"
# Mindep Domain_Id
Domain_Id = "07289f217a000f270f4ac0029ccd0a60"
# Va a IAM a obtener token
auth_url = "https://iam.myhuaweicloud.com/v3"
cloud = "myhuaweicloud.com"
#region = "ap-southeast-1"
AK = "URTVVDPSFIMWFZ5BRO5X"
SK = "zT8znL8fd2RkgFU1CDJWnflgod36LK9802TsZ8GX"

# Mindep
AKk = "PZBMXICI6IT4FZCN5NMQ"
SKk = "NmY7bnJjV3qxRYP4eQtsQ8y0PkXVhXQHAyCqNpjx"


# Me encontre esta URL de BSS, creo que es la que se usa como API.
# https://bss.example.com/v1.0


if __name__ == '__main__':

    # Entregar credencales al usuario
    conn = connection.Connection(
        auth_url=auth_url,
        #user_domain_id=userDomainId,
        domain_id=userDomainId,
        #username=username,
        #password=password,
        cloud = cloud,
        #region = region,
        ak = AK,
        sk = SK
    )

    """ 1 : devuelve el total de todo, y un total de un solo servicio.
    
    data = {
        "cycle": "2022-02",
        "cloud_service_type_code": "hws.service.type.ebs",
        "type": "1",
    }
    response = conn.bssintl.query_monthly_expenditure_summary(userDomainId, **data)
    print("RESPONSE: ",response)
    """

    """ 2 No funciona
    
    data = {
        "consume_month": "2022-02"
    }
    try:
        # bss-intl
        response = conn.bssintl.query_partner_monthly_bills(Domain_Id, **data)
        print("RESPONSE:",response)
    except Exception as error:
        print("Error: ", error)
    
    """
    
    url = "https://bss-intl.myhuaweicloud.com/v1.0//partner/account-mgr/postpaid-bill-summary?consume_month=2022-02"
    """
    url = "https://bss-intl.myhuaweicloud.com/v2/bills/partner-bills/postpaid-bill-summary?bill_cycle=2022-02"
    // curl --location --request GET 'https://bss-intl.myhuaweicloud.com/v1.0//partner/account-mgr/postpaid-bill-summary?consume_month=2022-02'
    headers = {'Content-Type': 'application/json', 'Access-Token':'', 'X-Auth-Token':''}
    """
    headers = {'Content-Type': 'application/json', 'charset':'', 'utf8':''}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.content)
    else:
        print("GET No")
    



    """print("\n-----------------------------------------------------------\n")
    def get_agency_list():
        agencies = conn.iam.agencies(domain_id=userDomainId)
        # agencies = conn.iam.agencies(domain_id=userDomainId, name="**********", trust_domain_id="**********")
        for agency in agencies:
            print("Agency:",agency)

    get_agency_list()"""
    
"""
# Create permanent accesskey
# POST /v3.0/OS-CREDENTIAL/credentials
def create_credential():
    credential = {
        "description": "ak/sk:acortes:hid_-d5rc...",
        "user_id": "5275c20af48b47adaa0f471e7269df1e"
    }
    credential = conn.iam.create_credential(**credential)
    print(credential)
"""