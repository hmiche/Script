import Functions
import time

data_path="ocr.txt"
with open(data_path, 'r',encoding="utf8") as file:
    res = file.read()
text = res.split("\n")  



depart=time.time()



Functions.extractnom(text)
Functions.Capital(text)
Functions.date(text)
Functions.form(text)
Functions.extractActivité(text)
Functions.siege(text)


print()
print()
print("temps dexecution est :"+str(time.time()-depart))

  