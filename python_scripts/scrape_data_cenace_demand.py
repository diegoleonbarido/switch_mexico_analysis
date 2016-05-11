import requests
from datetime import datetime
import json

url = 'http://cenace.gob.mx/GraficaDemanda.aspx/obtieneValoresTotal'
headers = {
        'Accept':'application/json, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control':'max-age=0',
        'Content-Type':'application/json;charset=UTF-8',
        'Host':'cenace.gob.mx',
        'Referer':' http://cenace.gob.mx/GraficaDemanda.aspx',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'X-Requested-With':'XMLHttpRequest',
        'Connection':'keep-alive',
        } 

for load_zone_data in range(1,11):
    
    values= "{'gerencia':" + "'" + str(load_zone_data) + "'}"
    s = requests.session()
    r = s.post(url, data=values,headers=headers)
    data = json.loads(r.content)
    
    if load_zone_data == 1:
        baja_norte = json.loads(data['d'])
    elif load_zone_data == 2:
        baja_sur = json.loads(data['d'])
    elif load_zone_data == 3:
        sin_central = json.loads(data['d'])
    elif load_zone_data == 4:
        sin_noreste = json.loads(data['d'])
    elif load_zone_data == 5:
        sin_noroeste = json.loads(data['d'])
    elif load_zone_data == 6:
        sin_norte = json.loads(data['d'])
    elif load_zone_data == 7:
        sin_occidental = json.loads(data['d'])
    elif load_zone_data == 8:
        sin_oriental = json.loads(data['d'])
    elif load_zone_data == 9:
        sin_peninsular = json.loads(data['d'])    
    elif load_zone_data == 10:
        sin = json.loads(data['d'])    
        
day_data_allzones = {"baja_norte" : baja_norte,"baja_sur": baja_sur,"sin_central":sin_central,"sin_noreste":sin_noreste,"sin_noroeste":sin_noroeste,"sin_norte":sin_norte,"sin_occidental":sin_occidental,"sin_oriental":sin_oriental,"sin_peninsular":sin_peninsular,"sin":sin}

with open(datetime.now().strftime("%d_%m_%Y_mexico")+'.txt', 'w') as outfile:
    json.dump(day_data_allzones, outfile)