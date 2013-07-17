from gi.repository import Gtk, Gio, GLib
from gnomemusic.window import Window


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id='org.gnome.Music',
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        GLib.set_application_name("Music")

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        self._window = Window(self)
        self._window.show()

    def quit(self):
        self.quit()
