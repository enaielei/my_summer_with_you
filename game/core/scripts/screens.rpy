screen say(who, what):
    window:
        id "window"
        bottom_margin 75
        xalign 0.5
        yalign 1.0

        vbox:
            if who is not None:

                window:
                    id "namebox"
                    background "#000"
                    padding (10, 5)
                    xalign 0.5

                    text who.upper() id "who"

            frame:
                background "#000"
                padding (10, 5)

                text what id "what"