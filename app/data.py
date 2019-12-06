import requests
#https://cloud.ibm.com/docs/tutorials?topic=solution-tutorials-serverless-api-webapp

def IBMcloudFunctions():
    response=requests.get("https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/6d4dfa15dfab1699968c8ef9d1a7d2012c86d144c4d8021d3a2959911882cde0/switches/entries")
    return(response.json())

def IBMcloudPost(data):
    response=requests.put(url="https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/6d4dfa15dfab1699968c8ef9d1a7d2012c86d144c4d8021d3a2959911882cde0/switches/entries", data=data)
    return(response.json())

"""
curl --request PUT \
  --url https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/6d4dfa15dfab1699968c8ef9d1a7d2012c86d144c4d8021d3a2959911882cde0/switches/entries/77cc3b09b734d717a16c0d0700d78b93 \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"name":"testing","slug":"QFX-5200","recommendedVersion":"junos 18.1R3-S6"}'
"""
