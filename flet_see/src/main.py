import flet as ft
import requests
import json
import time


def main(page: ft.Page):
    x = requests.get(url="http://localhost:8090/users")
    print(x.text)
    data = json.loads(x.text)
    for actual in data:
        r = ft.Row(controls=[ft.Image(src="/home/nightdragon/cosmonautica/flet_see/goyitlo.jpeg" , width=50 , height=50),
            ft.Text("identificador") , ft.Text(actual["idPer"]) , ft.Text("locactiones") , ft.Text(actual["location"]) , ft.Text("datos") , ft.Text(actual["data"])])
        page.add(r)
    page.update()
    while(True):
        r.controls.clear()
        x = requests.get(url="http://localhost:8090/users")
        data = json.loads(x.text)
        for actual in data:
            r.controls.append(ft.Image(src="/home/nightdragon/cosmonautica/flet_see/goyitlo.jpeg" , width=50 , height=50))
            r.controls.append(ft.Text("identificador"))
            r.controls.append(ft.Text(actual["idPer"]))
            r.controls.append(ft.Text("locactiones"))
            r.controls.append(ft.Text(actual["location"]))
            r.controls.append(ft.Text("datos"))
            r.controls.append(ft.Text(actual["data"]))
            page.update()
            time.sleep(0.7)
        




ft.app(main)
