# from urllib.request import urlopen
# from io import StringIO
# from io import open
#
# def readPDF(pdfFile):
#     rsrcmgr =
#     retstr = StringIO()
#     laparams =
#     device = TextConverter(rsrcmgr,retstr,laparams=laparams)
#
#     process_pdf(rsrcmgr, device, pdfFile)
#     device.close()
#
#     content = retstr.getvalue()
#     retstr.close()
#     return content
#
# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = readPDF(pdfFile)
# print(outputString)
# pdfFile.close()