from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json
import os

class FinanzasApp(App):
    def build(self):
        self.archivo = "data.json"
        self.total = self.cargar_total()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.monto = TextInput(
            hint_text="Monto",
            input_filter='float',
            multiline=False
        )

        self.resultado = Label(text=f"Total: {self.total}", font_size=24)

        btn_ingreso = Button(text="Agregar Ingreso")
        btn_ingreso.bind(on_press=self.agregar_ingreso)

        layout.add_widget(self.monto)
        layout.add_widget(btn_ingreso)
        layout.add_widget(self.resultado)

        return layout

    def cargar_total(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f).get("total", 0)
        return 0

    def guardar_total(self):
        with open(self.archivo, "w") as f:
            json.dump({"total": self.total}, f)

    def agregar_ingreso(self, instance):
        if self.monto.text:
            self.total += float(self.monto.text)
            self.resultado.text = f"Total: {self.total}"
            self.guardar_total()
            self.monto.text = ""

FinanzasApp().run()
