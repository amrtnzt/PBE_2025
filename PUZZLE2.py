import puzzle122
import threading
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class RfidApp:
    def __init__(self):
        self.window = Gtk.Window(title="UID Login App")
        self.window.set_border_width(10)
        self.window.set_default_size(400, 150)

        self.css_provider = Gtk.CssProvider()
        self.css_provider.load_from_path("windowstyle.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gtk.Window.get_screen(self.window),
            self.css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.window.add(vbox)

        self.label = Gtk.Label(label="Please, login with your UID card")
        self.label.get_style_context().add_class("yellow-label")
        vbox.pack_start(self.label, True, True, 0)

        self.clear_button = Gtk.Button(label="Clear")
        self.clear_button.connect("clicked", self.clear_label)
        self.clear_button.get_style_context().add_class("clear-button")

        vbox.pack_start(self.clear_button, True, True, 0)

        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

        self.start_uid_thread()

    def clear_label(self, button):
        self.label.set_text("Scann a new UID card to login")
        self.label.get_style_context().remove_class("blue-label")
        self.label.get_style_context().add_class("yellow-label")
        self.start_uid_thread()

    def start_uid_thread(self):
        thread = threading.Thread(target=self.read_uid_thread)
        thread.daemon = True
        thread.start()

    def read_uid_thread(self):
        rf = puzzle122.Rfid()
        uid = rf.read_uid()
        GLib.idle_add(self.update_label, uid)

    def update_label(self, uid):
        self.label.set_text(f"UID card read successfully: {uid}")
        self.label.get_style_context().remove_class("yellow-label")
        self.label.get_style_context().add_class("blue-label")

if __name__ == "__main__":
    app = RfidApp()
    Gtk.main()
