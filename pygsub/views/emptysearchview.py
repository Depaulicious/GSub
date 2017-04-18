# Copyright (c) 2016 The GSub Developers
#
# GSub is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# GSub is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with GSub; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# The GSub authors hereby grant permission for non-GPL compatible
# GStreamer plugins to be used and distributed together with GStreamer
# and GSub.  This permission is above and beyond the permissions
# granted by the GPL license by which GSub is covered.  If you
# modify this code, you may extend this exception to your version of the
# code, but you are not obligated to do so.  If you do not wish to do so,
# delete this exception statement from your version.

from gettext import gettext as _
from gi.repository import Gd, Gtk

from pygsub import log
from pygsub.toolbar import ToolbarState
from pygsub.views.baseview import BaseView


class EmptySearchView(BaseView):

    def __repr__(self):
        return '<EmptySearchView>'

    @log
    def __init__(self, window, player):
        BaseView.__init__(self, 'emptysearch', None, window, Gd.MainViewType.LIST)
        self._artistAlbumsWidget = None
        self._albumWidget = None
        self.player = player

        builder = Gtk.Builder()
        builder.add_from_resource('/eu/depau/GSub/NoMusic.ui')
        widget = builder.get_object('container')
        widget.set_vexpand(True)
        widget.set_hexpand(True)
        widget.get_children()[1].get_children()[1].set_text(_("Try a different search"))
        widget.show_all()
        self._box.add(widget)

    @log
    def _back_button_clicked(self, widget, data=None):
        self._header_bar.searchbar.show_bar(True, False)
        if self.get_visible_child() == self._artistAlbumsWidget:
            self._artistAlbumsWidget.destroy()
            self._artistAlbumsWidget = None
        elif self.get_visible_child() == self._grid:
            self._window.views[0].set_visible_child(self._window.views[0]._grid)
            self._window.toolbar.set_state(ToolbarState.CHILD_VIEW)
        self.set_visible_child(self._grid)
