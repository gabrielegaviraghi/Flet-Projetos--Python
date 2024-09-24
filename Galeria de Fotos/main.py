import flet as ft

def image(num: int):
    return ft.Image(
        src=f'https://picsum.photos/150/150?{num}', # imagens aleatórias
        fit= ft.ImageFit.COVER,
        repeat= ft.ImageRepeat.NO_REPEAT,
    )

def main(page: ft.Page):
    page.padding= 0
    page.window_title_bar_hidden= True

    # função ao clicar no botão
    def change_view(e):
        btn1.style = btn_style
        btn2.style = btn_style
        e.control.style = btn_style_selected
        # btn1.update()
        # btn2.update()

        if e.control.text == 'Agrupadas':
            layout.controls[0] = grid2
            page.padding= ft.padding.only(top=20)
        else:
            layout.controls[0] = grid1
            page.padding= 0

        page.update()

    grid1= ft.GridView(
        controls=[image(num) for num in range(110)],
        expand= True,
        runs_count=3,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    grid2 = ft.Column(
        expand=True,
        controls=[
            ft.Text(value='2022', size=30),
            ft.GridView(
                controls=[image(num) for num in range(1, 4)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            ),
            ft.Text(value='2023', size=30),
            ft.GridView(
                controls=[image(num) for num in range(10, 20)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            ),
            ft.Text(value='2024', size=30),
            ft.GridView(
                controls=[image(num) for num in range(5, 8)],
                runs_count=4,
                child_aspect_ratio=1.0,
                spacing=5,
                run_spacing=5,
            ),
        ]
    )

    # estilo do botão
    btn_style_selected = ft.ButtonStyle(
        bgcolor= ft.colors.BLACK54,
        color= ft.colors.WHITE,
        elevation= 0,
        overlay_color= ft.colors.BLACK12
    )

    btn_style= ft.ButtonStyle(
        bgcolor= ft.colors.TRANSPARENT,
        color= ft.colors.BLACK54,
        elevation= 0,
        overlay_color= ft.colors.BLACK12
    )

    # footer / botão
    footer= ft.Container(
        margin= ft.margin.symmetric(vertical=5, horizontal=10),
        padding= ft.padding.all(5),
        border_radius= ft.border_radius.all(50),
        bgcolor= ft.colors.WHITE70,
        content= ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            controls=[
                btn1 := ft.ElevatedButton(
                    text='Todas as fotos', 
                    style=btn_style_selected,
                    on_click= change_view,
                ),

                btn2 := ft.ElevatedButton(
                    text='Agrupadas', 
                    style=btn_style,
                    on_click= change_view,
                )
            ],
            tight=True, # juntar
        )
    )

    layout = ft.Column(
        expand= True,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        controls=[
            grid1,
            footer
        ]
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target= main)