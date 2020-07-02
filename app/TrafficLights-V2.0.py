#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

south = [2, 3, 4]
west = [14, 15, 18]
north = [17, 27, 22]
east = [23, 24, 25]
red = [2, 14, 17, 23]
yellow = [3, 15, 27, 24]
green = [4, 18, 22, 25]

all = south + west + north + east


def initialize():
    for led in all:
        GPIO.setup(led, GPIO.OUT)


def reset_all():
    for led in all:
        GPIO.output(led, GPIO.LOW)


def all_yellow():
    for led in yellow:
        GPIO.output(led, GPIO.HIGH)


def all_red():
    for led in red:
        GPIO.output(led, GPIO.HIGH)
    for led in yellow:
        GPIO.output(led, GPIO.LOW)
    for led in green:
        GPIO.output(led, GPIO.LOW)


def north_south_red():
    GPIO.output(north[0], GPIO.HIGH)
    GPIO.output(south[0], GPIO.HIGH)
    GPIO.output(north[1], GPIO.LOW)
    GPIO.output(south[1], GPIO.LOW)
    GPIO.output(north[2], GPIO.LOW)
    GPIO.output(south[2], GPIO.LOW)


def north_south_yellow():
    GPIO.output(north[0], GPIO.LOW)
    GPIO.output(south[0], GPIO.LOW)
    GPIO.output(north[1], GPIO.HIGH)
    GPIO.output(south[1], GPIO.HIGH)
    GPIO.output(north[2], GPIO.LOW)
    GPIO.output(south[2], GPIO.LOW)


def north_south_green():
    GPIO.output(north[0], GPIO.LOW)
    GPIO.output(south[0], GPIO.LOW)
    GPIO.output(north[1], GPIO.LOW)
    GPIO.output(south[1], GPIO.LOW)
    GPIO.output(north[2], GPIO.HIGH)
    GPIO.output(south[2], GPIO.HIGH)


def west_est_red():
    GPIO.output(west[0], GPIO.HIGH)
    GPIO.output(east[0], GPIO.HIGH)
    GPIO.output(west[1], GPIO.LOW)
    GPIO.output(east[1], GPIO.LOW)
    GPIO.output(west[2], GPIO.LOW)
    GPIO.output(east[2], GPIO.LOW)


def west_est_yellow():
    GPIO.output(west[0], GPIO.LOW)
    GPIO.output(east[0], GPIO.LOW)
    GPIO.output(west[1], GPIO.HIGH)
    GPIO.output(east[1], GPIO.HIGH)
    GPIO.output(west[2], GPIO.LOW)
    GPIO.output(east[2], GPIO.LOW)


def west_est_green():
    GPIO.output(west[0], GPIO.LOW)
    GPIO.output(east[0], GPIO.LOW)
    GPIO.output(west[1], GPIO.LOW)
    GPIO.output(east[1], GPIO.LOW)
    GPIO.output(west[2], GPIO.HIGH)
    GPIO.output(east[2], GPIO.HIGH)


def counters():
    GPIO.setwarnings(False)
    GPIO.setup(20, GPIO.IN)
    GPIO.setup(21, GPIO.IN)


def NS_way():
    north_south_green()
    time.sleep(10)
    north_south_yellow()
    time.sleep(2)
    north_south_red()
    west_est_green()
    time.sleep(10)
    west_est_yellow()
    time.sleep(2)
    west_est_red()


def WE_way():
    west_est_green()
    time.sleep(10)
    west_est_yellow()
    time.sleep(2)
    west_est_red()
    north_south_green()
    time.sleep(10)
    north_south_yellow()
    time.sleep(2)
    north_south_red()


initialize()
reset_all()
counters()

while True:
    if GPIO.input(20) == 0:
        print('Car detected ahead')
        NS_way()
    elif GPIO.input(21) == 0:
        print('Car detected ahead')
        WE_way()
    else:
        all_red()
