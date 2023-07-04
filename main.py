from config import *
import flet as ft

async def main(page : ft.Page):
    page.title = TITLE
    await page.add_async(ft.Text("It's CubeFlet"))

if __name__ == '__main__':
    ft.app(target=main)