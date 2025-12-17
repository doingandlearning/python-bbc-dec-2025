import requests  
import json

try:
  # make a web request
  # GET/POST/PATCH/PUT/DELETE
  response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu",
              # headers={"Authorization": "1234"},
              # json={}
              )

  response.raise_for_status()
  print(response)  # 200 -> OK   404 -> not found 
  # parse the data
  data = response.json()
  
  # do something iwth it!!!
  # persist to the file system
  with open("pikachu.txt", "w") as file:
    file.write(str(data))

  with open("pikachu.json", "w") as file:
    file.write(json.dumps(data, indent=2))
  
except Exception as e:
  print(e)
