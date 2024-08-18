define translation.names = {}

define translation.fonts = {}

init python in translation.strings:
    devlang = _("DevLang")
    renpy.store.translation.names[None] = devlang

    english = _("English")
    renpy.store.translation.names["en"] = english

init python in translation.strings:
    pass
