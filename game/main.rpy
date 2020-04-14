label start:
    $AudioLayer.start()
    scene bg subway fog
    show tee neutral at left
    show aiko neutral
    show mage neutral at right
    "None of them look familiar..."
    jump past
    jump present
    jump future
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
