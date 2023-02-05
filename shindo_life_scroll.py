import pygame,time,keyboard,os
pygame.mixer.init()
mu = pygame.mixer.Sound("music.mp3")
times = (("Narumaki Barrage","1:15","Great Narumaki Bridge","1/10"),("Saberu Suprise","1:50","Training Field","1/10"),("Spirit Spear","1:30","Training Field","1/7"),("Liquid Control","3:20","Haze","1/10"),("Flame Control","5:10","Ember","1/7"),("Shock Control","9:25","Nimbus","1/10"),("Stone Control","12:35","Obelisk","1/10"),("Air Control","7:15","Dunes","1/10"),("Su tailed Spirit","3:30","Dunes","1/10"),("Mao Tailed Spirit","3:10","Nimbus","1/10"),("Isu Tailed Spirit","9:30","Haze","1/10"),("Sun Tailed Spirit","11:30","Obelisk","1/10"),("Ku Tailed Spirit","12:10","Obelisk","1/10"),("Sei Tailed Spirit","10:10","Haze","1/10"),("Chu Tailed Spirit","7:10","Dunes","1/10"),("Gai Tailed Spirit","8:25","Nimbus","1/10"),("Kor Tailed Spirit","6:10","Ember","1/10"),("Rab tailed Spirit","4:20","Tempest","1/10"),("Bat Cursed Spirit","2:15","Forest of Embers","1/10"),("Reptile Cursed Spirit","12:20","Blaze","1/10"),("Spider Cursed Spirit","2:50","Training Field","1/10"),("Toad Cursed Spirit","1:20","Tempest","1/10"),("Demon Gate Spirit","3:30","Ember","1/8"),("Heavenly Spirit","6:45","Dunes","1/7"),("Vapor Inner Spirit","6:45","Dunes","1/7"),("Divination Spirit","2:20","Blaze","1/10"),("Jayramaki Frog Spirit","2:45","Ember","1/10"),("Snail Spirit Awaken","5:20","Obelisk","1/10"),("Cobra Spirit Awaken","2:35","Obelisk","1/10"),("Narumaki Toad Spirit","2:45","Ember","1/10"),("Mastered Rabbit Spirit","8:20","Dunes","1/10"),("Finite Strength Spirit","2:45","Training Field","1/10"),("Cobra Stretch Mode","7:45","Tempest","1/10"),("Obelisk Fate Spirit","7:30","Obelsik","1/10"),("Dunes Fate Spirit","4:30","Dunes","1/10"),("Nimbus Fate Spirit","8:10","Nimbus","1/10"),("Haze Fate Spirit","6:20","Haze","1/10"),("Ember Fate Spirit","5:25","Ember","1/10"),("Specialist Spirit","5:35","Ember","1/10"),("Demonic Spirit","2:45","Haze","1/8"),("Shock Cloak","7:35","Nimbus","1/10"),("Akuma Eternal Hand","12:20","Ember","1/10"),("Santa Platinum Winter","1:15","Nimbus","1/10"),("Puppet Platinum Halloween","8:20","Dunes","1/10"),("Captian Jokei","5:30","Obelisk","1/10"),("Reality Talk","5:35","Blaze","1/10"),("Tree illusion Technique","7:15","Ember","1/10"),("Confusion Illusion Technique","8:10","1/10"),("Peekaboo Jutsu","11:20","Training Field","1/10"),("Clown Trap Halloween","12:25","Nimbus","1/10"),("Medical Mode-Transfer","11:35","Ember","1/10"),("Vanshing Clone: Barrage","4:40","Ember","1/7"),("Multi Vanishing Clones","12:25","Ember","1/6"),("Exploding Vanishing Image","6:30","Embers","1/10"),("Water Vanishing Image","5:15","Obelisk","1/6"),("Wood Vanishing Image","3:10","Nimbus","1/10"),("Narumaki Vanishing Clone","2:10","Great Narumaki Bridge","1/5"),("Narumaki Vanishing Multi-Clone","3:25","Great Narumaki Bridge","1/7"),("Vanishing Image","2:45","Ember","1/8"),("Shadow Snowman","2:45","Obelisk","1/5"),("Korashi Multi-Summon","8:15","Dawn Hideout","1/10"),("Heavenly Wall","3:10","Obelisk","1/10"),("Eagle Companion","9:15","Nimbus","1/10"),("Reaper Spirit","8:25","Forest of Embers","1/10"),("Scarecrow Seal Halloween","10:35","Dunes","1/10"),("Toad Summon","11:20","Tempest","1/10"),("Snake Summon","3:35","Tempest","1/10"),("Senko: Spirit Bomb","4:15","Ember","1/10"),("Senko: Storm","5:40","Obelisk","1/10"),("Shock Style: Dual Electro","2:45","Forest of Embers","1/10"),("Vanishing Spirit Bomb","4:23","Forest of Embers","1/6"),("Air Style: Odama Spirit Bomb","1:30","Training Field","1/8"),("Super Odama Spirit Bomb","2:45","Forest of Embers","1/10"),("Spirit Bomb-Shuriken Rush","2:45","Ember","1/6"),("Spirit Bomb-Shuriken Toss","2:45","Nimbus","1/10"),("Great Spiraling Spirit Bomb","12:15","Great Narumaki Bridge","1/10"),("Shockslam Technique","3:35","Obelisk","1/10"),("Lightning Shurikens","10:10","Training Field","1/5"),("Fire Shurikens","9:30","Forest of Embers","1/5"),("Demon Warp","2:45","Forest of Embers","1/6"),("Firework Subjutsu","10:20","Dunes","1/10"),("Rab Style: Warp","3:13","Obelisk","1/10"),("Rab Style: Prison","2:15","Haze","1/10"),("Rab Style: Meteorite","6:55","Obelisk","1/10"),("Sleigh Summon","7:15","Ember","1/10"),("Sleigh Bomb","6:35","Nimbus","1/10"))
while 1:
    hour = time.gmtime()[3]-7
    min = str(time.gmtime()[4])
    if int(min) < 10:
        min = "0"+min
    if hour > 12:
        current_arizona_time = str(hour-12)+":"+min
    else:
        current_arizona_time = str(hour)+":"+min
    print("Current Time:",current_arizona_time)
    for item in times:
        a,b = item[1].split(":")
        a = int(a)
        if a < 4:
            a = a+9
        else:
            a = a-3
        if int(b)-10 < 10:
            item_time = str(a)+":0"+str(int(b[:-3:-1][::-1])-10)
        else:
            item_time = str(a)+":"+str(int(b[:-3:-1][::-1])-10)
        if item_time == current_arizona_time:
            print("Name:",item[0])
            print("Time:",item[1])
            print("Location:",item[2])
            print("Probability of Spawning:",item[3])
            mu.stop()
            mu.play()
            input(".")
        print(item_time)
    time.sleep(20)