import matplotlib.pyplot as plt
import random
import secrets
import numpy as np
import time

def create_roulette(sizes, labels):
    # 룰렛 그릴 크기 설정
    plt.figure(figsize=(8, 8))
    
    # 각 조각의 시작 각도를 12시에서 시작하도록 설정
    start_angle = 90
    
    # 룰렛 그리기
    pie = plt.pie(sizes, labels=labels, startangle=start_angle, counterclock=False, autopct='%1.1f%%', colors=None)
    
    # 원형으로 출력
    plt.axis('equal')
    
    # 화살표 추가
    arrow_angle = 90  # 12시 방향
    arrow_length = 0.6  # 화살표 길이
    plt.arrow(0, 0.5, 0, 0.4, width=0.03, head_width=0.1, head_length=0.1, fc='r', ec='r')
    
    # 그래프 보여주기
    plt.show()

    # 룰렛 회전
    rotation_time = random.uniform(20, 25)  # 랜덤한 회전 시간 (3~10초)
    start_time = time.time()
    
    # 초기 회전 속도
    #initial_angular_velocity = random.uniform(30, 50)
    angular_velocity = random.uniform(25, 45) #initial_angular_velocity
    
    while time.time() - start_time < rotation_time:
        start_angle += angular_velocity  # 회전 각도 변화량
        plt.clf()  # 기존의 그래프를 지우고
        pie = plt.pie(sizes, labels=labels, startangle=start_angle, counterclock=False, autopct='%1.1f%%', colors=None)  # 새로운 각도로 룰렛 그리기
        
        # 화살표 추가
        plt.arrow(0, 0.5, 0, 0.4, width=0.03, head_width=0.1, head_length=0.1, fc='r', ec='r')
        
        plt.axis('equal')
        plt.draw()
        plt.pause(0.005)  # 그래프 업데이트 속도를 빠르게 함
        
        # 회전 속도 감속
        angular_velocity = 0.993 * angular_velocity #* initial_angular_velocity
        
        # 회전 속도가 음수가 되지 않도록 보정
        if angular_velocity < 0:
            angular_velocity = 0

    # 회전이 끝나면 멈추도록 대기
    plt.pause(2)

# 룰렛 조각의 크기와 라벨 설정
#sizes = [10, 20, 30, 40]
#labels = ['Piece 1', 'Piece 2', 'Piece 3', 'Piece 4']

# 룰렛 생성
#create_roulette(sizes, labels)
