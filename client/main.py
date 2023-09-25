import requests
import upnpy




upnp = upnpy.UPnP()
device = upnp.get_igd()
service = device['WANPPPConnection.1']
service.AddPortMapping(
    NewRemoteHost='',
    NewExternalPort=80,
    NewProtocol='TCP',
    NewInternalPort=8000,
    NewInternalClient='192.168.1.3',
    NewEnabled=1,
    NewPortMappingDescription='Test port mapping entry from UPnPy.',
    NewLeaseDuration=0
)





for i in range(0, 100):
    r = requests.get('http://127.0.0.1:8080/Python')

    print(r.status_code)
    print(r.encoding)
    print(r.text)
    print(r.json)