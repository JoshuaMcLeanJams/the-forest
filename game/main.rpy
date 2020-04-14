define e = Character("Eileen", color="#C8FFC8")

define audio.bass = "audio/running_genesis_bass.ogg"
define audio.bass2 = "audio/running_genesis_bass2.ogg"
define audio.drum = "audio/running_genesis_drum.ogg"
define audio.pulse1 = "audio/running_genesis_pulse1.ogg"
define audio.pulse2 = "audio/running_genesis_pulse2.ogg"
define audio.wave = "audio/running_genesis_wave.ogg"

image bg forest = "images/bg/fantasy-forest.png"
image bg bedroom = "images/bg/arabian-bedroom.png"
image bg subway = "images/bg/subway-morning.jpg"
image bg lakeside = "images/bg/lakeside-daytime.jpg"
image bg school = "images/bg/modern-school.png"

image mage neutral = "images/spr/mage_neutral.png"
image mage smile = "images/spr/mage_smile.png"

image tee neutral = "images/spr/tee_neutral.png"
image tee smile = "images/spr/tee_smiling.png"

image aiko smile = "images/spr/aiko_casual_smile.png"

init python:
    AudioLayer.set('drum', audio.drum)
    AudioLayer.set('bass', audio.bass)
    AudioLayer.set('bass2', audio.bass2)
    AudioLayer.set('pulse1', audio.pulse1)
    AudioLayer.set('pulse2', audio.pulse2)
    AudioLayer.set('wave', audio.wave)

label start:
    $AudioLayer.start()
    scene bg lakeside
    show tee smile at left
    show aiko smile
    show mage smile at right
    "Testing"
    nvl show

label main:
    nvl clear
    menu:
        "What shall we toggle?"

        "Bass":
            $AudioLayer.toggle('bass')
        "Bass 2":
            $AudioLayer.toggle('bass2')
        "Drum":
            $AudioLayer.toggle('drum')
        "Pulse 1":
            $AudioLayer.toggle('pulse1')
        "Pulse 2":
            $AudioLayer.toggle('pulse2')
        "Wave":
            $AudioLayer.toggle('wave')
        "Enable all":
            $AudioLayer.enable_all()
        "Disable all":
            $AudioLayer.disable_all()
        "Toggle all":
            $AudioLayer.toggle_all()
        "I'm outta here":
            jump end

    jump main

label end:
    "The End"
    $AudioLayer.stop()
    return
