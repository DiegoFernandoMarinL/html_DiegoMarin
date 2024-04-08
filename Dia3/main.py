from tabulate import tabulate
import requests

peticion = requests.get("http://localhost:5501")
data = peticion.json()
print(print(tabulate(data,headers="keys",tablefmt="html")))