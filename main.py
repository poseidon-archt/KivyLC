from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
from datetime import datetime
import shutil

Builder.load_string('''
<StoragePathInterface>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                text: 'External Storage'
                on_press: root.create_file(app.external_storage_path)
            Button:
                text: 'Documents'
                on_press: root.create_file(app.documents_path)
        BoxLayout:
            Button:
                text: 'Downloads'
                on_press: root.create_file(app.downloads_path)
            Button:
                text: 'Pictures'
                on_press: root.create_file(app.pictures_path)

<StoragePathApp>:
    StoragePathInterface:
''')

class StoragePathInterface(BoxLayout):
    def create_file(self, directory):
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except PermissionError:
                # Fallback sur le répertoire de l'application si les permissions sont insuffisantes
                directory = App.get_running_app().user_data_dir

        filename = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as f:
            f.write("This is a test file created by the app.")

        print(f"File created: {filepath}")

class StoragePathApp(App):
    external_storage_path = os.path.join(os.environ.get('EXTERNAL_STORAGE'), 'DCIM/ze')
    documents_path = os.path.join(os.environ.get('EXTERNAL_STORAGE'), 'Documents')
    downloads_path = os.path.join(os.environ.get('EXTERNAL_STORAGE'), 'Downloads')
    pictures_path = os.path.join(os.environ.get('EXTERNAL_STORAGE'), 'Pictures')

    def build(self):
        return StoragePathInterface()

if __name__ == "__main__":
    StoragePathApp().run()
