label start:
    $AudioLayer.start()
    scene bg subway fog
    show tee neutral at left
    show aiko neutral
    show mage neutral at right

    "None of them look familiar..."
    "Judging by the looks on their faces, you're not familiar to them, either."

    menu:
        "Talk to the woman in green":
            hide tee 
            hide aiko with dissolve
            show mage neutral at center with move
            m "Yes?"
        "Talk to the girl in the tee-shirt":
            hide mage 
            hide aiko with dissolve
            show tee neutral at center with move
            t "Yes?"
        "Talk to the girl in the uniform":
            hide tee 
            hide mage with dissolve
            show aiko neutral at center with move
            a "Yes?"

    jump end

label past:
    scene bg past day
    show mage neutral
    "A mage in the day"
    scene bg past night
    show mage happy
    "A mage at night"

label present:
    scene bg modern school
    show aiko neutral
    "A school..."
    scene bg modern street
    show aiko happy
    "Some street"

label future:
    scene bg future space
    show tee neutral
    "We're in a tunnel"
    scene bg future med station
    show tee happy
    "Is this a med station?"

label end:
    return
