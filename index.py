from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class CalorieCounter(App):
    def calculate_calories(self, instance):
        try:
            weight = float(self.weight_input.text)
            height = float(self.height_input.text)
            age = float(self.age_input.text)
            # Простой пример расчета калорий
            calorie_intake = 10 * weight + 6.25 * height - 5 * age + 5
            self.result_label.text = f"Рекомендуемое потребление калорий: {calorie_intake}"
        except ValueError:
            self.result_label.text = "Пожалуйста, введите корректные данные"

    def build(self):
        layout = GridLayout(cols=1, padding=10)
        
        self.weight_input = TextInput(hint_text='Вес (кг)')
        self.height_input = TextInput(hint_text='Рост (см)')
        self.age_input = TextInput(hint_text='Возраст')
        
        calculate_button = Button(text='Рассчитать калории', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        calculate_button.bind(on_press=self.calculate_calories)
        
        self.result_label = Label(text='', halign='center')
        
        layout.add_widget(self.weight_input)
        layout.add_widget(self.height_input)
        layout.add_widget(self.age_input)
        
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(calculate_button)
        layout.add_widget(anchor_layout)
        
        layout.add_widget(self.result_label)
        
        return layout

if __name__ == '__main__':
    CalorieCounter().run()
