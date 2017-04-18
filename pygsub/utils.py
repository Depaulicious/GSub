# Copyright (c) 2016 Marinus Schraal <mschraal@src.gnome.org>
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


def get_album_title(item):
    """Returns the album title associated with the media item

    In case of an audio file the get_album call returns the
    album title and in case of a container we are looking for
    the title.

    :param item: A Grilo Media object
    :return: The album title
    :rtype: string
    """
    album = item.get_album()

    if not album:
        album = get_media_title(item)

    return album


def get_artist_name(item):
    """Returns the preferred artist for a media item.

    The artist name for a particular media item can be either
    the main artist of the full album (album artist), the
    artist of the song (artist) or possibly it is not known at
    all. The first is preferred in most cases, because it is
    the most accurate in an album setting.

    :param item: A Grilo Media object
    :return: The artist name
    :rtype: string
    """

    return (item.get_album_artist()
            or item.get_artist()
            or _("Unknown Artist"))


def get_media_title(item):
    """Returns the title of the media item.

    :param item: A Grilo Media object
    :return: The title
    :rtype:
    """

    return (item.get_title()
            or _("Untitled"))


def seconds_to_string(duration):
    """Convert a time in seconds to a mm:ss string

    :param int duration: Time in seconds
    :return: Time in mm:ss format
    :rtype: string
    """
    seconds = duration
    minutes = seconds // 60
    seconds %= 60

    return '{:d}:{:02d}'.format(minutes, seconds)
