# -*- coding: utf8 -*-
import RPi.GPIO as GPIO
import time
from infloop import infloop

pinLeds = (26, 16, 21, 20) # 시계방향으로 핀 목록을 작성

GPIO.setmode(GPIO.BCM) # GPIO번호를 BCM기준으로, BOARD는 보드에 핀순서
for pin in pinLeds:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW) # 각 핀을 OUTPUT, LOW로 초기화

try:
    for pin in infloop(pinLeds): # 시계방향 순서로
        GPIO.output(pin, GPIO.HIGH) # LED를 켜고
        time.sleep(1.0) # 1초 후에
        GPIO.output(pin, GPIO.LOW) # LED를 끈다
except: # 프로그램 강제 종료 시
    for pin in pinLeds: # 모든 핀의
        GPIO.output(pin, GPIO.LOW) # LED를 끈다
    GPIO.cleanup() # GPIO 출력 설정 초기화