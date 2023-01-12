
import sys
import ssl
import http.client
import mimetypes
import logging
# supress ssl errors
ssl._create_default_https_context = ssl._create_unverified_context

logging.critical(("file_arguments_list: ", sys.argv))
payload = ''
headers = {}
mac_address = sys.argv[1]
apiKey = 'at_Mco4shjRDxlrBdMY2TQXNLBqjlEWW'


class macapi():

    def __init__(self, mac_address, apiKey):
        self.mac_address = mac_address
        self.apiKey = apiKey

    def macaddress_api(self, mac_address, apiKey):
        conn = http.client.HTTPSConnection("api.macaddress.io")
        conn.request("GET", f"/v1?apiKey={apiKey}&output=json&search=" + mac_address, payload, headers)
        res = conn.getresponse()
        data = res.read()
        return logging.critical(data.decode("utf-8"))

macapi_class = macapi(mac_address, apiKey)
instantiate_func = macapi_class.macaddress_api(mac_address, apiKey)
