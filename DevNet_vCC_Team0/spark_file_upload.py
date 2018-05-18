import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder({'roomId': '<ID>',
                      'text': 'example attached',
                      'files': ('sample.pdf', open('sample.pdf', 'rb'),
                      'application/pdf')})

r = requests.post('https://api.ciscospark.com/v1/messages', data=m,
                  headers={'Authorization': 'Bearer <TOKEN>',
                  'Content-Type': m.content_type})

print (r.text)
