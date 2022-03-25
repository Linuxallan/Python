from openstack import connection
import json
import sys
from openstack import utils
utils.enable_logging(debug=False,stream=sys.stdout)

""" SDK V3 (new)
# Regional services
basic_credentials = BasicCredentials(ak, sk, project_id)

# Global services
global_credentials = GlobalCredentials(ak, sk, domain_id)

# Con token
# Regional services
basic_credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)

# Global services
global_credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
"""

# Crear connection
username = 'acortes'
password = 'huame82gus_'
# Poryect ID de la region de 'Santiago'
projectId = '0ebc7a689c00f2c72f85c01d5d3ebaf5'
# domain_id is the account ID of Huawei Cloud.
userDomainId = '605ff9aef384489ab0c518dba4535b5e'
# auth_url = 'iam.sa-chile-1.myhuaweicloud.com/v3'
# auth_url = 'iam.la-sur-2.myhuaweicloud.com/'
auth_url = 'https://iam.sa-chile-1.myhuaweicloud.com/v3'

# Conexion
conn = connection.Connection(
    auth_url = auth_url,
    user_domain_id = userDomainId,
    project_id = projectId,
    username = username,
    password = password,
    # verificacion de cliente
    verify=True
)

# Set parameter
limit = 5

def list_servers():
    try:
        servers = conn.compute.servers(limit=limit)
        print(servers)
        response = []
        for server in servers:
            response.append(server)
        
        return response[0]
        
    except Exception as error:
        print(error)
        return "Error"

res = list_servers()
print(res)

"""
serv = json.dumps(ser)
file = open('response_json.json', 'wb')
file.write(serv)
file.close()
"""