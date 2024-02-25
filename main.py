from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import os
from datetime import datetime

Builder.load_string('''
#: import storagepath plyer.storagepath
<StoragePathInterface>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            Button:
                text: 'Home'
                on_press: root.create_file(storagepath.get_home_dir())
            Button:
                text: 'External Storage'
                on_press: root.create_file(storagepath.get_external_storage_dir())
        BoxLayout:
            Button:
                text: 'Root'
                on_press: root.create_file(storagepath.get_root_dir())
            Button:
                text: 'Documents'
                on_press: root.create_file(storagepath.get_documents_dir())
        BoxLayout:
            Button:
                text: 'Downloads'
                on_press: root.create_file(storagepath.get_downloads_dir())
            Button:
                text: 'Videos'
                on_press: root.create_file(storagepath.get_videos_dir())
        BoxLayout:
            Button:
                text: 'Music'
                on_press: root.create_file(storagepath.get_music_dir())
            Button:
                text: 'Pictures'
                on_press: root.create_file(storagepath.get_pictures_dir())
        Button:
            text: 'Applications'
            on_press: root.create_file(storagepath.get_application_dir())

<StoragePathApp>:
    StoragePathInterface:
''')


class StoragePathInterface(BoxLayout):
    def create_file(self, directory):
        dcim_path = os.path.join(directory, 'DCIM/ze')
        filename = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filepath = os.path.join(dcim_path, filename)
        with open(filepath, 'w') as f:
            f.write("This is a test file created by the app.")
        print(f"File created: {filepath}")


class StoragePathApp(App):
    def build(self):
        return StoragePathInterface()


if __name__ == "__main__":
    StoragePathApp().run()
