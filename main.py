from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class CalculadoraApp(App):
    def build(self):
        self.title = "Minha Calculadora"
        
        # Variável para salvar a última conta realizada
        self.ultima_conta = "Nenhuma conta salva"
        
        # Layout principal vertical
        layout_principal = BoxLayout(
            orientation='vertical', 
            padding=20, 
            spacing=12
        )
        
        # Display da calculadora personalizado
        self.display = TextInput(
            text="0",
            font_size=48,
            halign="right",
            readonly=True,
            multiline=False,
            size_hint=(1, 0.20),
            background_color=get_color_from_hex('#1E1E2C'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            cursor_color=get_color_from_hex('#FFFFFF')
        )
        layout_principal.add_widget(self.display)
        
        # Botão especial para exibir/rever a última conta salva
        self.btn_ultima = Button(
            text="Última Conta: Nenhuma",
            font_size=15,
            size_hint=(1, 0.07),
            background_normal='',
            background_color=get_color_from_hex('#3A3A4F'),
            color=get_color_from_hex('#00FFCC')
        )
        self.btn_ultima.bind(on_press=self.mostrar_ultima_conta)
        layout_principal.add_widget(self.btn_ultima)
        
        # Layout de botões em grade (4 colunas)
        grid_botoes = GridLayout(
            cols=4, 
            spacing=10, 
            size_hint=(1, 0.65)
        )
        
        # Lista organizada de botões da calculadora
        botoes = [
            'C', '(', ')', '÷',
            '7', '8', '9', 'x',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]
        
        for texto in botoes:
            if texto == '':
                btn = Button(text='', disabled=True, background_color=(0,0,0,0))
            else:
                if texto in ['÷', 'x', '-', '+', '=']:
                    bg_color = get_color_from_hex('#FF7A00') # Laranja para operadores
                elif texto == 'C':
                    bg_color = get_color_from_hex('#E53935') # Vermelho para limpar
                else:
                    bg_color = get_color_from_hex('#2D2D3D') # Cinza para números

                btn = Button(
                    text=texto, 
                    font_size=28,
                    bold=True,
                    background_normal='',
                    background_color=bg_color,
                    color=get_color_from_hex('#FFFFFF')
                )
                btn.bind(on_press=self.on_button_click)
            
            grid_botoes.add_widget(btn)
            
        layout_principal.add_widget(grid_botoes)
        
        # Assinatura sutil e visível no rodapé
        assinatura = Label(
            text="Por:www.tiagodata.com.br",
            font_size=13,
            size_hint=(1, 0.04),
            color=get_color_from_hex('#7A7A99'), # Tom sutil acinzentado/azulado
            halign="center"
        )
        layout_principal.add_widget(assinatura)

        return layout_principal

    def on_button_click(self, instance):
        texto = instance.text
        atual = self.display.text
        
        if texto == 'C':
            self.display.text = "0"
        elif texto == '=':
            try:
                expressao = atual.replace('x', '*').replace('÷', '/')
                resultado = str(eval(expressao))
                
                if resultado.endswith('.0'):
                    resultado = resultado[:-2]
                
                self.ultima_conta = f"{atual} = {resultado}"
                self.btn_ultima.text = f"Última: {self.ultima_conta}"
                self.display.text = resultado
            except Exception:
                self.display.text = "Erro"
        else:
            if atual == "0" or atual == "Erro":
                self.display.text = texto
            else:
                self.display.text = atual + texto

    def mostrar_ultima_conta(self, instance):
        if self.ultima_conta != "Nenhuma conta salva":
            partes = self.ultima_conta.split("=")
            self.display.text = partes[1].strip()

if __name__ == '__main__':
    CalculadoraApp().run()

#copilação apk

