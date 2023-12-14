import requests
import json

api_key='API_KEY'    #https://app.ipgeolocation.io/dashboard
URL="https://api.ipgeolocation.io/ipgeo?"
IP=input("IP ADRESINI GIRIN= ")

fields="country_name"  

#diğer fields seçenekleri 
#fields="ip"             
#fields="hostname"       
#fields="continent_code" 
#fields="continent_name" 
#fields="country_code2"  
#fields="country_code3"  
#fields="country_name"   
#fields="country_capital"
#fields="state_prov"     
#fields="district"       
#fields="city"           
#fields="zipcode"        
#fields="latitude"       
#fields="longitude"      
#fields="is_eu"          
#fields="calling_code":
#fields="country_tld"    
#fields="languages"      
#fields="country_flag"   
#fields="isp"            
#fields="connection_type"
#fields="organization"   
#fields="asn":
#fields="geoname_id"     
#fields="currency"       
#fields="time_zone"

r = requests.get(URL+"&apiKey="+api_key+"&ip="+IP+"&fields="+fields)
#Birden fazla fields için request e ekleme yapmanız gerek. Örn: 3 fields için +"&fields="+fields kodunu 3 kere eklemen gerek
 
data = r.text
output = json.loads(data)

print(output.get('country_name'))  #Bu alanı da hangi çıktıları almak istediğinize göre değiştirmeniz gerek. 

