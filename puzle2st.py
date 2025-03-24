import puzzle122
import threading
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class RfidApp:
    def __init__(self):
        self.window = Gtk.Window(title="RFID Login")
        self.window.set_border_width(10)
        self.window.set_default_size(400, 100)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.window.add(vbox)
        self.label = Gtk.Label(label="Please, login with your university card")
        vbox.pack_start(self.label, True, True, 0)
        self.clear_button = Gtk.Button(label="Clear")
        self.clear_button.connect("clicked", self.clear_label)
        vbox.pack_start(self.clear_button, True, True, 0)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
        self.start_uid_thread()

    def clear_label(self, button):
        self.label.set_text("Apropa la targeta per al login.")
        self.start_uid_thread()

    def start_uid_thread(self):
        thread = threading.Thread(target=self.read_uid_thread)
        thread.daemon = True  
        thread.start()

    def read_uid_thread(self):
        rf=puzzle122.Rfid() 
        uid =rf.read_uid() 
        #print (f"{uid}")
        GLib.idle_add(self.update_label, uid)

    def update_label(self, uid):
        """Actualiza el label con el UID leído."""
        self.label.set_text(f"UID read successfully: {uid}")

if __name__ == "__main__":
    app = RfidApp()
    Gtk.main()

