import flet as ft
import time
import requests
import json


def main(page: ft.Page):
    x = requests.get(url="http://localhost:8090/getDataSensor")
    print(x.text)
    col = ft.Column()
    datos = json.loads(x.text)
    for d in datos:
        r = ft.Row(controls=[
            ft.Text("datos:") , ft.Text(d["data"]),
            ft.Text("nombre:") , ft.Text(d["name"])
        ])
        col.controls.append(r)
    page.add(col)
    page.update()
    while(True):
            xa = requests.get(url="http://localhost:8090/getDataSensor")
            datos2 = json.loads(xa.text)
            print(xa.text)
            for a in range(0,len(col.controls)):
                 col.controls[a].controls[1].text = datos2[a]["data"]
                 col.controls[a].controls[3].text = datos2[a]["name"]
            page.update()
            time.sleep(1)
            
            






    


ft.app(main)
