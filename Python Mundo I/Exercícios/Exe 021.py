import pygame

pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\anael\OneDrive\Área de Trabalho\Python\Guanabara\Exercícios\exe021.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

#pygame.mixer.music.set_volume(0.5)