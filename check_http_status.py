# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# match = """[{"type":"invalid url"}]"""
#
# url = "http://portal.osmani.com:8049/0033-OCL-2020-WS/linker.php"
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# soup = str(soup)
# # print(soup)
# # print(type(soup))
# if soup == match:
#     print("done!")
# else:
#     print("not")


import urllib
response = urllib.request.urlopen("https://kite.com")
status_code = response.getcode()

print(status_code)
