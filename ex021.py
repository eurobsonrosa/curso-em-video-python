print('='*20+' REPRODUDOR MP3 '+'='*20)
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
