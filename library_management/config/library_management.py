from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Library"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Book",
                    "label": _("Book"),
                    "description": _("Books which members issue and return."),
                },
                {
                    "type": "doctype",
                    "name": "Library Member",
                    "label": _("Library Member"),
                    "description": _("People whohave enrolled for membership in the library."),
                },
                {
                    "type": "doctype",
                    "name": "Library Membership",
                    "label": _("Library Membership"),
                    "description": _("People who have taken membership for the library"),
                },
                {
                    "type": "doctype",
                    "name": "Library Transaction",
                    "label": _(""),
                    "description": _("Issuing an article or returning a book are the transactions taking place."),
                }
            ]
        }
    ]
