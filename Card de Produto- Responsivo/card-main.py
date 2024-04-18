import flet as ft

def main(page: ft.Page):
    page.bgcolor = '#000000',
    page.scroll= ft.ScrollMode.AUTO,
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #alterar a opacidade e a foto dos elementos ao clicar
    def change_main_image(e):
        for elem in options.controls: #verifica se o elemento é o elem da função
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src #substitui a imagem principal
            else:
                elem.opacity = 0.5
        #atualizando as alterações
        main_image.update()
        options.update()
    
    # parte esquerda do card = imagens
    product_images = ft.Container(
        col={'xs':12, 'md':6},
        bgcolor= '#FFFFFF',
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[ #adicionando as imagens
                main_image := ft.Image( #walrus operator
                    src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                ),
                options := ft.Row( #imagens secundárias (parte de baixo)
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_942879-MLU71482713005_092023-O.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_908128-MLU72835305161_112023-O.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )

    # adicionando a parte direita do card = detalhes do produto com opções
    product_details = ft.Container(
        col={'xs':12, 'md':6}, #reponsividade 
        padding= ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(value='CADEIRAS', 
                        color='#FFBF00', 
                        weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Poltrona Amarela Moderna',
                    color='#FFFFFF',
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Sala de estar',
                    color='#808080',
                    italic=True
                ),

                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER, #centralizar o valor com as estrelas
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm':6}, #colocar ao lado das estrelas, responsivo a telas pequenas e grandes
                            value='R$ 399', 
                            color='#FFFFFF', 
                            size=30
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm':6}, #ao lado do valor, responsivo
                            wrap=False, #não quebra as estrelas
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR, 
                                    color='#FFBF00' if _ < 4 else '#FFFFFF' #escolher quantas estrelas vão ser amarelas e brancas
                                ) for _ in range(5) #vai repetir 5x as estrelas
                            ] 
                        )
                    ]
                ),
                #abas de navegação
                ft.Tabs(
                    height = 150,
                    selected_index=0, # indice da aba para aparecer primeiro
                    indicator_color = '#FFBF00', # cor da barra
                    label_color = '#FFBF00', # cor da palavra da tab
                    unselected_label_color = '#808080', #cor da aba não selecionada
                    tabs=[
                        ft.Tab(  # aba específica
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='A poltrona Decorativa Amamentação Cadeira Reforçada Opala Bege Cor Amarelo Desenho do Tecido Suede é perfeita para criar um ambiente moderno e aconchegante na sua casa. Com sue design retrô e cor amarela vibrante.',
                                    color='#808080',
                                    text_align=ft.TextAlign.JUSTIFY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Dimensões: 0.8m de largura, 0.9m de altura e 0.76m de profundidade. \n\nMaterial dos pés: Eucalipto.',
                                    color='#808080'
                                )
                            )
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6, #vai ocupar metade da row 12/2 = 6
                            label='Cor',
                            label_style=ft.TextStyle(color='#FFFFFF', size=16),
                            border_color='#808080',
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Amarelo'),
                                ft.dropdown.Option(text='Azul'),
                                ft.dropdown.Option(text='Cinza')
                            ]
                        ),
                        ft.Dropdown(
                            col=6, #vai ocupar metade da row 12/2 = 6
                            label='Quantidade',
                            label_style=ft.TextStyle(color='#FFFFFF', size=16),
                            border_color='#808080',
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} unid') for num in range(1, 11)
                            ]
                        )
                    ]
                ),

                #vai ocupar o espaço que sobrou no meio 
                ft.Container(expand=True), 

                # adicionando o botão da lista de desejos
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejos',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color='#FFFFFF')#borda padrão do default será de...
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: '#FFFFFF' #vai trocar de cor ao passar o mouse
                        },
                        color={
                            ft.MaterialState.DEFAULT: '#FFFFFF', #cor de texto padrão
                            ft.MaterialState.HOVERED: '#000000' #cor de texto muda ao passar o mouse
                        }
                    )
                ),
                # adicionando o botão de carrinho
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color='#FFBF00'),
                            ft.MaterialState.HOVERED: ft.BorderSide(width=2,color='#FFCF3F')
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: '#FFBF00',
                            ft.MaterialState.HOVERED: '#FFCF3F'
                        },
                        color={
                            ft.MaterialState.DEFAULT: '#000000',
                        }
                    )
                )

            ]
        )
        
    )

    # criando o layout principal
    layout = ft.Container(
        width=850,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color= '#00FFFF'),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[ # criando a parte esquerda e direita do card
                product_images,
                product_details
            ]
            
        )

    )
    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)