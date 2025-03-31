import flet as ft
import requests
import json


def main(page: ft.Page):
    x = requests.get(url="http://localhost:8090/users")
    print(x.text)
    data = json.loads(x.text)
    for actual in data:
        r = ft.Row(controls=[ft.Image(src="/home/nightdragon/cosmonautica/flet_see/goyitlo.jpeg" , width=50 , height=50),
            ft.Text("identificador") , ft.Text(actual["userId"]) , ft.Text("locactiones") , ft.Text(actual["location"]) , ft.Text("datos") , ft.Text(actual["data"])])
        page.add(r)
    page.update()


ft.app(main)
