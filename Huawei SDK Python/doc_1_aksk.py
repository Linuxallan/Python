from openstack import connection
import sys
from openstack import utils
utils.enable_logging(debug=True,stream=sys.stdout)

projectId = "0ebece24a100900c2f66c01d85051860"
cloud = "myhuaweicloud.com"
region = "ap-southeast-1"
AK = "URTVVDPSFIMWFZ5BRO5X"
SK = "zT8znL8fd2RkgFU1CDJWnflgod36LK9802TsZ8GX"

conn = connection.Connection(
    project_id = projectId,
    cloud = cloud,
    region = region,
    ak = AK,
    sk = SK
)

# Parametros pre definidos
# limit : especifica un limite de datos (tuplas) que retornara
# la peticion.
limit = 5
# ----
# ignore_missing: si al elimnar algo ese no existe -->
# False --> lanza la excepcion correspondiente y detiene la ejecucion.
# True --> pasa por alto la ejecucion fallida y sigue solamente.
# ignore_missing = True/False
# ----
# Obtener mas detalles en la respuesta de la solicitud.
# details = True/False
def test_compute():

    try:
        servers = conn.compute.servers(limit=limit)

        for server in servers:
            print(server)
        
    except Exception as error:
        print(error)

if __name__ == '__main__':
    
    test_compute()