
import http.client

conn = http.client.HTTPSConnection("walmart-jp-wfmr-b.jdadelivers.com")

payload = "loginName=Dokada&password=c123456"

headers = {
    'cache-control': "no-cache",
    'postman-token': "7ae263bc-061f-4f5e-df6d-d2368ae4169c"
    }

conn.request("GET", "/Retail/data/retailwebapi/api/v1-beta3/jobs?siteIdFilter=1000104", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))