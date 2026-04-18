from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import subprocess
import os

class BotLauncherApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(text="Trading Bot Launcher", font_size='20sp', size_hint=(1, 0.3))
        self.status = Label(text="Tap START to launch bot in Termux", font_size='14sp', size_hint=(1, 0.2))
        
        start_btn = Button(text="START BOT", size_hint=(1, 0.3), background_color=(0.2, 0.6, 0.2, 1))
        start_btn.bind(on_press=self.start_bot)
        
        layout.add_widget(title)
        layout.add_widget(self.status)
        layout.add_widget(start_btn)
        
        return layout

    def start_bot(self, instance):
        # Path to app.py inside Termux (adjust if needed)
        # Default: /data/data/com.termux/files/home/storage/shared/App.py/app.py
        # Or use a simple command that runs from home directory
        command = "cd ~/storage/shared/App.py && python app.py &"
        
        # Use termux-open to start Termux and run the command
        # Alternative: broadcast intent
        intent = "am start -n com.termux/com.termux.app.TermuxActivity -e command \"{}\"".format(command)
        try:
            subprocess.Popen(intent, shell=True)
            self.status.text = "Bot launching in Termux..."
            Clock.schedule_once(lambda dt: self.update_status(), 3)
        except Exception as e:
            self.status.text = f"Error: {e}"
    
    def update_status(self):
        self.status.text = "Bot started. Switch to Termux to monitor."

if __name__ == '__main__':
    BotLauncherApp().run()
