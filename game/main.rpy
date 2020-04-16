label start:
    #$AudioLayer.start()
    play music longing

    scene bg future space
    show tee neutral at left
    t "We're gonna be late, get moving!"

    menu:
        "Late for what?":
            show tee annoyed at center with move
            t "Ugh, you're hopeless. Come on."
            "She grabs you by the arm and you have no choice but to follow."
        "Okay, let's go!":
            show tee happy at center with move
            t "Thank you."
            show tee happy at right with move
            "She heads down the hall and you follow."

    show tee at right with move
    hide tee with dissolve

    scene bg future med bay
    show tee neutral at left with dissolve
    t "You first."
    "She motions toward the machine in the center of the room."

    menu:
        "She's tapping her foot impatiently."

        "Why am I first?":
            show tee angry
            t "Because you don't know how to operate it, duh. Now get in."

        "What is this thing?":
            show tee annoyed
            t "Don't ask stupid questions. Get in."

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
            m "It's me, you dingbat."
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
    scene bg past day
    play music forest
    "Where am I now?"
    show mage neutral at left
    "There she is again. She looks around."
    show mage relieved at left
    t "Oh, that's better."
    show mage neutral
    t "Now gather some twigs. I'll look around for shelter."
    hide mage dissolve
    "She disappears before you can protest, or even ask any questions."
    "Why are you gathering twigs?"
    "Guess you should do what Boss Sister says... as usual."
    $twigs = 0
    $turns = 0

label gathering:
    $import random
    menu:
        "Gather twigs (have [twigs])":
            $twigs_found = random.randint(1, 3)
            $twigs += twigs_found
            "You find [twigs_found] twigs and add them to your stockpile."
            $turns += 1
        "Wait a while":
            "You lean against a tree and wait for a bit."
            $turns += 1
    if turns >= 6:
        jump gathering_done
    jump gathering

label gathering_done:
    show mage neutral
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

    $asked_twigs = False
    menu:
        "Why do we need twigs?" if not asked_twigs:
            $asked_twigs = True
            show mage annoyed
            t "To build a fire, obviously."
        "Did you find any shelter?":
            t "Yep, there's a cave not far from here."

    show mage neutral
    t "Let's get moving."
    "You trek to the cave."
    hide mage with dissolve

    scene bg past night
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
        "She claps her hands."
        jump ending_bad
    elif twigs < 3:
        t "That's... it?"
        show mage sad
        t "I guess I could try..."
        "She snaps her fingers over the twigs and they ignite, providing light
        and warmth..."
        "...for about ten seconds."
        show mage angry
        "She claps her hands without another word."
        jump ending_bad
    elif twigs < 9:
        t "I guess that'll do."
        "She snaps her fingers over the twigs and they ignite."
        jump ending_neutral
    else:
        show mage happy
        t "Oh, excellent."
        "She snaps her fingers over the twigs and they ignite."
        jump ending_good

label ending_bad:
    scene bg subway night
    play music longing
    "You're back in that strange tube thing, but now it's moving."
    "Patiently, you wait for your sister to appear."
    "The minutes pass and... nothing."
    "You wonder if you'll ever get out."
    "(Bad ending, 1/3)"
    jump end

label ending_neutral:
    "The warmth is enough to get you through the night. And then the real
    journey begins..."
    "(Neutral ending, 2/3)"
    jump end

label ending_good:
    "The two of you stay up all night seeing amazing visions in the
    flames. It's almost like watching a vidscreen."
    "A wonderful bond forms that will last the rest of your lives."
    "(Good ending, 3/3)"
    jump end

label end:
    "THE END"
    return
