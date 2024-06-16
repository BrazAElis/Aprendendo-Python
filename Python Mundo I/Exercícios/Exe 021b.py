import pygame

audio_file_name = 'exe021.mp3'
pygame.mixer.init()
pygame.mixer.music.load(audio_file_name)
pygame.mixer.music.play()
input()
pygame.event.wait()

# pygame.mixer.music.set_volume(0.5)
