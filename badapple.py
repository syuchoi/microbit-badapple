def trackChord():
    global playChord
    for index in range(2):
        loopMelody2()
        music.play_tone(156, music.beat(BeatFraction.HALF))
        music.play_tone(185, music.beat(BeatFraction.QUARTER))
        music.play_tone(156, music.beat(BeatFraction.QUARTER))
        music.play_tone(208, music.beat(BeatFraction.HALF))
        music.play_tone(185, music.beat(BeatFraction.QUARTER))
        music.play_tone(208, music.beat(BeatFraction.QUARTER))
        loopMelody2()
        music.play_tone(208, music.beat(BeatFraction.HALF))
        music.play_tone(185, music.beat(BeatFraction.QUARTER))
        music.play_tone(208, music.beat(BeatFraction.QUARTER))
        music.play_tone(185, music.beat(BeatFraction.HALF))
        music.play_tone(156, music.beat(BeatFraction.QUARTER))
        music.play_tone(185, music.beat(BeatFraction.QUARTER))
    for index2 in range(3):
        loopMelody3()
    loopMelody2()
    music.play_tone(156, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(156, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    for index3 in range(2):
        # 낮은 시
        music.play_tone(123.47, music.beat(BeatFraction.HALF))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        # 낮은 라#
        music.play_tone(116.54, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(156, music.beat(BeatFraction.HALF))
    music.play_tone(156, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.HALF))
    for index4 in range(3):
        loopMelody4()
    for index5 in range(2):
        # 낮은 시
        music.play_tone(123.47, music.beat(BeatFraction.HALF))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        # 낮은 라#
        music.play_tone(116.54, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(165, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(185, music.beat(BeatFraction.HALF))
    music.play_tone(165, music.beat(BeatFraction.QUARTER))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    loopMelody2()
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.play_tone(185, music.beat(BeatFraction.WHOLE))
    playChord = False
def sndDrum(duration: number, repeat: number):
    for index6 in range(repeat):
        music.play_tone(100, 10)
        music.rest(duration)
# Chord용 반복 1
def loopMelody2():
    for index7 in range(3):
        music.play_tone(156, music.beat(BeatFraction.HALF))
        music.play_tone(156, music.beat(BeatFraction.QUARTER))
        music.play_tone(156, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        music.play_tone(156, music.beat(BeatFraction.QUARTER))
        music.play_tone(139, music.beat(BeatFraction.QUARTER))
        music.play_tone(156, music.beat(BeatFraction.QUARTER))

def on_button_pressed_a():
    global isPlaying
    isPlaying = 1
    playBadApple()
input.on_button_pressed(Button.A, on_button_pressed_a)

def loopMelody1():
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.play_tone(698, music.beat(BeatFraction.HALF))
    music.play_tone(740, music.beat(BeatFraction.HALF))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
    music.play_tone(1244, music.beat(BeatFraction.HALF))
    music.play_tone(1108, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
    music.play_tone(622, music.beat(BeatFraction.WHOLE))
    music.play_tone(932, music.beat(BeatFraction.HALF))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(740, music.beat(BeatFraction.HALF))
    music.play_tone(698, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.HALF))
    music.play_tone(698, music.beat(BeatFraction.HALF))
    music.play_tone(740, music.beat(BeatFraction.HALF))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(740, music.beat(BeatFraction.HALF))
def trackBeat():
    global playBeat
    for index8 in range(2):
        for index9 in range(3):
            sndDrum(music.beat(BeatFraction.WHOLE), 3)
            sndDrum(music.beat(BeatFraction.QUARTER), 4)
            sndDrum(music.beat(BeatFraction.WHOLE), 3)
            sndDrum(music.beat(BeatFraction.HALF), 2)
        sndDrum(music.beat(BeatFraction.WHOLE), 3)
        sndDrum(music.beat(BeatFraction.QUARTER), 4)
        sndDrum(music.beat(BeatFraction.WHOLE), 4)
    playBeat = False
# Chord용 반복 2
def loopMelody3():
    loopMelody2()
    music.play_tone(156, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(156, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    for index10 in range(2):
        # 낮은 시
        music.play_tone(123.47, music.beat(BeatFraction.HALF))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        # 낮은 라#
        music.play_tone(116.54, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(156, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(156, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
# Chord용 반복 3
def loopMelody4():
    for index11 in range(2):
        # 낮은 시
        music.play_tone(123.47, music.beat(BeatFraction.HALF))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
        # 낮은 라#
        music.play_tone(116.54, music.beat(BeatFraction.QUARTER))
        music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(123.47, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.HALF))
    music.play_tone(165, music.beat(BeatFraction.QUARTER))
    music.play_tone(139, music.beat(BeatFraction.QUARTER))
    music.play_tone(185, music.beat(BeatFraction.HALF))
    music.play_tone(165, music.beat(BeatFraction.QUARTER))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    loopMelody2()
    music.play_tone(156, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(156, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(185, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))

def on_button_pressed_ab():
    trackChord()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def trackMain():
    for index12 in range(2):
        loopMelody1()
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(622, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(740, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(622, music.beat(BeatFraction.HALF))
        music.play_tone(587, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        loopMelody1()
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        music.play_tone(740, music.beat(BeatFraction.WHOLE))
        music.play_tone(831, music.beat(BeatFraction.WHOLE))
        music.play_tone(932, music.beat(BeatFraction.WHOLE))
    for index13 in range(3):
        for index14 in range(2):
            music.play_tone(1108, music.beat(BeatFraction.HALF))
            music.play_tone(1244, music.beat(BeatFraction.HALF))
            music.play_tone(932, music.beat(BeatFraction.HALF))
            music.play_tone(831, music.beat(BeatFraction.HALF))
            music.play_tone(932, music.beat(BeatFraction.WHOLE))
            music.play_tone(831, music.beat(BeatFraction.HALF))
            music.play_tone(932, music.beat(BeatFraction.HALF))
        music.play_tone(831, music.beat(BeatFraction.HALF))
        music.play_tone(740, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(554, music.beat(BeatFraction.HALF))
        music.play_tone(622, music.beat(BeatFraction.WHOLE))
        music.play_tone(554, music.beat(BeatFraction.HALF))
        music.play_tone(622, music.beat(BeatFraction.HALF))
        music.play_tone(698, music.beat(BeatFraction.HALF))
        music.play_tone(740, music.beat(BeatFraction.HALF))
        music.play_tone(831, music.beat(BeatFraction.HALF))
        music.play_tone(932, music.beat(BeatFraction.HALF))
        music.play_tone(622, music.beat(BeatFraction.WHOLE))
        music.play_tone(831, music.beat(BeatFraction.HALF))
        music.play_tone(932, music.beat(BeatFraction.HALF))
    music.play_tone(1108, music.beat(BeatFraction.HALF))
    music.play_tone(1244, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.HALF))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.HALF))
    music.play_tone(1108, music.beat(BeatFraction.HALF))
    music.play_tone(1244, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.HALF))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
    music.play_tone(1244, music.beat(BeatFraction.HALF))
    music.play_tone(1396, music.beat(BeatFraction.HALF))
    music.play_tone(1479, music.beat(BeatFraction.HALF))
    music.play_tone(1396, music.beat(BeatFraction.HALF))
    music.play_tone(1244, music.beat(BeatFraction.HALF))
    music.play_tone(1108, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.WHOLE))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(932, music.beat(BeatFraction.HALF))
    music.play_tone(831, music.beat(BeatFraction.HALF))
    music.play_tone(740, music.beat(BeatFraction.HALF))
    music.play_tone(698, music.beat(BeatFraction.HALF))
    music.play_tone(554, music.beat(BeatFraction.HALF))
    music.play_tone(622, music.beat(BeatFraction.WHOLE))

def on_button_pressed_b():
    global isPlaying
    if isPlaying == 1:
        isPlaying = 2
        while isPlaying == 2:
            music.stop_melody(MelodyStopOptions.ALL)
            basic.clear_screen()
    if isPlaying == 2:
        isPlaying = 1
        music.set_volume(150)
        while isPlaying == 1:
            basic.show_string("BADAPPLE")
input.on_button_pressed(Button.B, on_button_pressed_b)

def playBadApple():
    global playBeat, playChord
    playBeat = True
    for index15 in range(8):
        music.rest(music.beat(BeatFraction.BREVE))
    playChord = True
    for index16 in range(8):
        music.rest(music.beat(BeatFraction.BREVE))
    trackMain()
playChord = False
playBeat = False
isPlaying = 0
music.set_tempo(138)
music.set_built_in_speaker_enabled(True)
music.set_volume(150)
isPlaying = 0
playBeat = False
playChord = False
basic.show_icon(IconNames.YES)
basic.pause(500)
basic.clear_screen()

def on_forever():
    while isPlaying == 1:
        basic.show_string("BADAPPLE")
basic.forever(on_forever)

def on_forever2():
    while playBeat == True:
        trackBeat()
basic.forever(on_forever2)

def on_forever3():
    while playChord == True:
        trackChord()
basic.forever(on_forever3)
