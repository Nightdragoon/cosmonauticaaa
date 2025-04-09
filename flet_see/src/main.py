import flet as ft
import requests
import json
import time


def main(page: ft.Page):
    x = requests.get(url="http://localhost:8090/users")
    print(x.text)
    data = json.loads(x.text)
    c = ft.Column()
    for actual in data:
        r = ft.Row(controls=[ft.Image(src="/home/nightdragon/cosmonautica/flet_see/goyitlo.jpeg" , width=50 , height=50),
            ft.Text("identificador") , ft.Text(actual["idPer"]) , ft.Text("locaciones") , ft.Text(actual["location"]) , ft.Text("datos") , ft.Text(actual["data"])])
        c.controls.append(r)
    page.add(c)
    page.update()
    while(True):
        c.controls.clear()
        x2 = requests.get(url="http://localhost:8090/users")
        data2 = json.loads(x2.text)
        for actual in data2:
            r2 = ft.Row(controls=[ft.Image(src="/home/nightdragon/cosmonautica/flet_see/goyitlo.jpeg" , width=50 , height=50),
            ft.Text("identificador") , ft.Text(actual["idPer"]) , ft.Text("locaciones") , ft.Text(actual["location"]) , ft.Text("datos") , ft.Text(actual["data"])])
            c.controls.append(r2)
        page.update()
        time.sleep(0.7)
        




ft.app(main)
