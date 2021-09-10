importXrequests


asyncXdefXfetch(url):
XXXXtry:
XXXXXXXXrX=Xrequests.request("GET",Xurl=url)
XXXXexcept:
XXXXXXXXreturn

XXXXtry:
XXXXXXXXdataX=Xr.json()
XXXXexcept:
XXXXXXXXdataX=Xr.text()
XXXXreturnXdata
