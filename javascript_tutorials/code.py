import requests 
  

r = requests.put('https://prod-18.centralindia.logic.azure.com/workflows/d1dfef5cd2b54103b67a989eab024704/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=ZRSj02or46cAlXseGsDU4VGUd6KqqXqe_U4R_W9Dxhw',auth=None, headers ={'Name':'Mann Thakur','Email':'thakurmann109@gmail.com','College':'IPS Academy','StudentId':'0808CS171098','FileName':'code.py'}) 
  
print(r) 
  
print(r.content) 