init python in translation.strings:
    pass

define translation.names = {}

define translation.fonts = {}

init python in translation.strings:
    devlang = _("DevLang")
    renpy.store.translation.names[None] = devlang

init python in translation.strings:
    english = _("English")
    renpy.store.translation.names["en"] = english