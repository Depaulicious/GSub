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

from pygsub import log
from pygsub.albumartcache import ArtSize
from pygsub.views.emptyview import EmptyView


class InitialStateView(EmptyView):

    def __repr__(self):
        return '<InitialStateView>'

    @log
    def __init__(self, window, player):
        EmptyView.__init__(self, window, player)

        # Update image
        icon = self.builder.get_object('icon')
        icon.set_margin_bottom(32)
        icon.set_opacity(1)
        icon.set_from_resource('/eu/depau/GSub/initial-state.png')
        icon.set_size_request(ArtSize.large.width, ArtSize.large.height)

        # Update label
        label = self.builder.get_object('label')
        label.set_label(_("Hey DJ"))
        label.set_opacity(1)
        label.set_margin_bottom(18)
