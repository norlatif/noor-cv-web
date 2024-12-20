from nicegui import ui

def button_clicked():
    ui.notify('Button clicked!')

ui.label('Hello World').classes('text-h3')
ui.button('Click me!', on_click=button_clicked)

ui.run(reload=True)
