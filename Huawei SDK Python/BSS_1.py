from openstack import connection
import sys
import json
from openstack import utils
utils.enable_logging(debug=False,stream=sys.stdout)

username = "acortes"
password = "huame82gus_"
userDomainId = "605ff9aef384489ab0c518dba4535b5e"
# Va a IAM a obtener token
auth_url = "https://iam.myhuaweicloud.com/v3"
cloud = "myhuaweicloud.com"
#region = "ap-southeast-1"
AK = "URTVVDPSFIMWFZ5BRO5X"
SK = "zT8znL8fd2RkgFU1CDJWnflgod36LK9802TsZ8GX"

# Me encontre esta URL de BSS, creo que es la que se usa como API.
# https://bss.example.com/v1.0

if __name__ == '__main__':
    conn = connection.Connection(
        auth_url=auth_url,
        user_domain_id=userDomainId,
        #domain_id=userDomainId,
        #username=username,
        #password=password,
        cloud = cloud,
        #region = region,
        ak = AK,
        sk = SK
    )

    """ 1 : devuelve el total de todo, y un total de un solo servicio.
    
    data = {
        "cycle": "2022-01",
        "cloud_service_type_code": "hws.service.type.ebs",
        "type": "1"
    }
    response = conn.bssintl.query_monthly_expenditure_summary(userDomainId, **data)
    print("RESPONSE: ",response)
    """

    """ 2 No funciona
    """
    data = {
        "consume_month": "2022-02"
    }
    try:

        response = conn.bssintl.query_partner_monthly_bills(userDomainId, **data)
        print("Res:",response)
    except Exception as error:
        print("Error: ", error)
    