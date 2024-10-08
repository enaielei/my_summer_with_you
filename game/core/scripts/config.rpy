## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("My Summer with You")

## The version of the game.

define config.version = "1.0.0"

## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

init python:
    if config.developer:
        config.save_directory = None
    else:
        config.save_directory = "enaielei/my_summer_with_you"

## The icon displayed on the taskbar or dock.

# define config.window_icon = "gui/window_icon.png"