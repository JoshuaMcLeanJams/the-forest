label start:
    #$AudioLayer.start()
    play music longing fadein 3.0 fadeout 1.0

    scene bg future space with vpunch

    show tee neutral at left
    "Your sister is pushier than usual today."
    t "Move! We need to get this done."

    $choice1 = True
label menu1:
    menu:
        "Late for what?" if choice1:
            $choice1 = False
            show tee annoyed at center with move
            t "Ugh, you're hopeless. Come on."
            jump menu1
        "Okay, let's go!":
            show tee happy at center with move
            t "Thank you."
            show tee happy at right with move
            "She heads down the hall and you follow."

    show tee at right with move
    hide tee with dissolve

    scene bg future med bay with hpunch
    show tee neutral at left with dissolve
    t "You first."
    "She motions toward the machine in the center of the room."

    $choice1 = True
    $choice2 = True
label menu2:
    menu:
        "She's tapping her foot impatiently."

        "Why am I first?" if choice1:
            show tee angry
            t "Because you don't know how to operate it, duh. Now get in."
            jump menu2
        "What is this thing?" if choice1:
            show tee annoyed
            t "Don't ask stupid questions. We're running out of time."
            jump menu2
        "Okay.":
            show tee neutral
            t "All right, lay down and get the straps on."

    "You do as she says."

    show tee sad
    t "Comfy?"

    "She doesn't give you time to answer and presses a ton of buttons
    on the console in quick succession."

    scene bg subway fog with fade

    "You're in a strange tube-shaped vehicle that doesn't appear to be moving."
    "The fog outside clouds any view of your location."

    show mage neutral at left with dissolve
    "A strange woman appears and looks around."

    show mage suspicious 
    m "Wait, this isn't right."

    show mage annoyed
    m "Ugh, did you do this? Did you tamper with the machine?"

    menu:
        m "Well, did you?"

        "Yep, I did":
            show mage angry
            m "Typical."

        "Uh... no?":
            show mage sad
            m "*sigh* Well maybe it was a freak accident."

        "Wait, who are you?":
            m "It's me, you donut."
            "You don't recognize her at all."
            show mage angry
            m "Your sister! Agh, do I have to explain this every time?"
            "She takes a deep breath."
            show mage neutral
            m "This is my avatar in the virtual world. See, look at you!"
            "You look down and see your clothes have changed, as has your
            figure."
            "Right! You remember. This is the reflection of your best
            self from your mind."
            "...that explains why you're so fit."
            show mage sad
            t "Guess you get it now. Anyway, something is wrong. This isn't the
            right place."
            jump fix

    "You're still not used to your sister looking different in the virtual
    world, but it's obvious why she wants to look like a mage."
    "It's a power trip."
    "...not that you're much better, your avatar impossibly fit."

label fix:
    t "Let me fix it."
    hide mage with dissolve

label vr:
    scene bg past day with fade
    play music forest fadein 1.0
    "Where am I now?"
    show mage neutral at left
    "There she is again. She looks around."
    show mage relieved at left
    t "Oh, that's better."
    show mage neutral
    t "Now gather some twigs. I'll look around for shelter."
    show mage at right with move
    hide mage dissolve
    "She disappears before you can protest, or even ask any questions."
    "Why are you gathering twigs?"
    "Guess you should do what Boss Sister says... as usual."

label gather_start:
    $twigs = 0
    $turns = 0

label gathering:
    menu:
        "Gather twigs (you have [twigs])":
            $twigs_found = random.randint(1, 3)
            $twigs += twigs_found
            "You find [twigs_found] twigs and add them to your stockpile."
            $turns += 1
        "Wait a few minutes":
            "You lean against a tree and wait."
            $turns += 1
        "Wait for her to return":
            $turns += 10
    if turns >= 6:
        jump gathering_done
    jump gathering

label gathering_done:
    show mage neutral at right with dissolve
    t "You done?"

    if twigs == 0:
        "She doesn't seem to notice you gathered nothing."
    # none = 0
    # half = 3-9
    # every turn = 6-18
    if twigs == 0:
        "She doesn't seem to notice you gathered nothing."
    elif twigs < 3:
        "Your pile is miserable, but she doesn't notice."
    elif twigs < 9:
        "You've got a decent stack of twigs but she doesn't bother to look."
    elif twigs < 15:
        "You gathered quite the pile of twigs. She doesn't seem to care."
    else:
        "Argh! You did an amazing job, and she won't even look at your stack of
        twigs."

    $choice1 = True
label menu3:
    menu:
        "Why do we need twigs?" if choice1:
            $choice1 = False
            show mage annoyed
            t "To build a fire, obviously."
            jump menu3
        "Did you find any shelter?":
            t "Yep, there's a cave not far from here."

    show mage neutral
    t "Let's get moving."
    "You trek to the cave."
    hide mage with dissolve

    scene bg past night with fade
    show mage neutral with dissolve
    t "Okay, drop the twigs there."
    if twigs > 0:
        "You drop your pile of [twigs] twigs."

    if twigs == 0:
        t "..."
        show mage sad
        t "Wait, where are the twigs?"
        show mage angry
        t "YOU DIDN'T GET ANY?!"
        jump return_to_forest
    elif twigs < 3:
        t "That's... it?"
        show mage sad
        t "I guess I could try..."
        "She snaps her fingers over the twigs and they ignite, providing light
        and warmth..."
        "...for about ten seconds."
        jump return_to_forest
    elif twigs < 9:
        t "I guess that'll do."
        "She snaps her fingers over the twigs and they ignite."
        jump ending
    else:
        show mage happy
        t "Oh, excellent."
        "She snaps her fingers over the twigs and they ignite."
        jump ending

label return_to_forest:
    show mage angry
    "She claps."
    scene bg past day with fade
    "You're back out in the forest. Oddly, it's daytime again."
    show mage angry with dissolve
    "Now get some damn twigs!"
    hide mage with dissolve
    jump gather_start

label ending:
    stop music fadeout 2.0
    "A strange white light begins piercing through the forest around you."

    show mage suspicious
    t "This is it!"

    hide mage with dissolve
    show tee happy with dissolve
    t "See, we're losing our avatars."

label end:
    scene bg future space with fadewhite
    play music longing fadein 3.0
    show tee happy with dissolve
    t "Okay, that's all I needed you for. Get back to your room."
    show tee at right with move
    hide tee with dissolve
    "Before you can protest, she disappears down the hall."
    "What was that all about?"
    "You'll find out soon enough..."

label end_end:
    "THE END"
    jump end_end
    return
