from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDLabel:
        id: track_label
        text: "Track"
        halign: 'center'
        font_style: 'H5'
        size_hint_y: None
        height: self.texture_size[1]

    MDRaisedButton:
        text: "Show Image"
        on_release: app.show_image()

    Image:
        id: image
        source: ""
        size_hint: None, None
        size: "200dp", "200dp"
        center_x: root.width / 2
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_image(self):
        # Load and display the image when the button is clicked
        self.root.ids.image.source = "car.png"  # Replace with the actual path to your image

if __name__ == "__main__":
    MyApp().run()
