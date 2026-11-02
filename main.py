import pygame
import time
import os

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("song.mp3")

lyrics = [
    "🌸 Keno je eto bhalobasha more jaay... 💔",
    "🕰️  Shudhu shomoy mone rakhe... 🥀",
    "🌧️  Eto shunnota e mone rakhi je ami... 💭",
    "😔 Dekhe na keu to aar, bole e sobi pagolami.... 💔",
    "🌙 Kate Na Jamini... 🥀",
    "💔 Biroho Jeno Kete Jay... 🌧️",
    "🌧️  Thame Na Borsha... 💙",
    "❤️  Tomare Daki Je Ami....... 🥺"
]

timings = [
    [0.0, 4.0],
    [4.0, 7.0],
    [8.0, 12.0],
    [12.0, 16.0],
    [16.0, 18.0],
    [18.0, 20.0],
    [21.0, 22.0],
    [23.0, 26.0]
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_lyrics():
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000

        clear_screen()

        print("\n🎧 Now Playing: Long Distance Love | Coke Studio Bangla\n")

        for i, line in enumerate(lyrics):
            start, end = timings[i]

            if current_time >= end:
                print(line)

            elif current_time >= start:
                progress = (current_time - start) / (end - start)
                characters = int(progress * len(line))
                print(line[:characters])

            else:
                break

        time.sleep(0.03)

try:
    show_lyrics()
finally:
    pygame.mixer.music.stop()
    pygame.quit()