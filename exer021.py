# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()  # iniciar o paygame
pygame.mixer.music.load('musicateste.mp3')
pygame.mixer.music.play()
pygame.event.wait()