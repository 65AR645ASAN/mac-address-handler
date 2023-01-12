import json
import sys
import ssl
import http.client
import mimetypes
import logging
# supress ssl errors
ssl._create_default_https_context = ssl._create_unverified_context

# logging.critical(("file_arguments_list: ", sys.argv))
payload = ''
headers = {}
mac_address = sys.argv[1]
apiKey = 'at_Mco4shjRDxlrBdMY2TQXNLBqjlEWW' # retrieve the API key from the maclookup website provided for email adi.sandhu@outlook.com


class macapi():

    def __init__(self, mac_address, apiKey):
        self.mac_address = mac_address
        self.apiKey = apiKey

    def macaddress_api(self, mac_address, apiKey):
        conn = http.client.HTTPSConnection("api.macaddress.io")
        conn.request("GET", f"/v1?apiKey={apiKey}&output=json&search=" + mac_address, payload, headers)
        res = conn.getresponse()
        data = res.read()
        dict_resp = json.loads(data.decode("utf-8"))
        return logging.critical(f"companyName >>> {dict_resp['vendorDetails']['companyName']}")

# instantiate class and func to return company name
macapi_class = macapi(mac_address, apiKey)
instantiate_func = macapi_class.macaddress_api(mac_address, apiKey)
