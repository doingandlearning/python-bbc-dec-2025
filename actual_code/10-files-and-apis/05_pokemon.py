import requests  
import json
API_KEY="TEST"
try:
  # make a web request
  # GET/POST/PATCH/PUT/DELETE
  response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu",
              headers={"Authorization": f"Bearer {API_KEY}", 
                      "Content-Type": "application/json"},
              json={}
              )

  response.raise_for_status()
  print(response)  # 200 -> OK   404 -> not found 
  # parse the data
  data = response.json()

  print(data["forms"][0]["name"])
  print(data["sprites"]["front_default"])
  
  # do something with it!!!
  # persist to the file system
  with open("pikachu.txt", "w") as file:
    file.write(str(data))

  with open("pikachu.json", "w") as file:
    file.write(json.dumps(data, indent=2))
  
except Exception as e:
  print(e)
