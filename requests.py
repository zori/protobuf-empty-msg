from requests_pb2 import *

def demo():
  r = Request()
  # Try to add the tagging extension.
  # r.Extensions[TaggingRequest.tagging]
  r.Extensions[TaggingRequest.tagging].Clear()
  try:
    r.Extensions[TaggingRequest.tagging].SetInParent()
  except AttributeError as e:
    print e  # 'TaggingRequest' object has no attribute 'SetInParent'

  print 'has tagging extension', r.HasExtension(TaggingRequest.tagging)

  # Add the numbered extension by setting its `number' field.
  r.Extensions[NumberedRequest.numbered].number = 42
  print 'has numbered extension', r.HasExtension(NumberedRequest.numbered)
  print 'NumberedRequest field', r.Extensions[NumberedRequest.numbered].number

demo()
