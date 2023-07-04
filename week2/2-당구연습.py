def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        # 1. 좌표 정리
        nx1 = ball[0] + 2*(m-ball[0])
        nx2 = ball[0] - 2*(ball[0])
        ny1 = ball[1] + 2*(n-ball[1])
        ny2 = ball[1] - 2*(ball[1])
        
        # 2. 제곱 계산
        len_x1 = (nx1 - startX)**2 + (ball[1] - startY)**2
        len_x2 = (nx2 - startX)**2 + (ball[1] - startY)**2
        len_y1 = (ny1 - startY)**2 + (ball[0] - startX)**2
        len_y2 = (ny2 - startY)**2 + (ball[0] - startX)**2
        
        # 3. 최소 length 구하기
        if startX == ball[0]:
            if startY > ball[1]:
                length = [len_x1, len_x2, ((n-startY)+(n-ball[1]))**2]
            else:
                length = [len_x1, len_x2, (startY + ball[1])**2]
        elif startY == ball[1]:
            if startX > ball[0]:
                length = [len_y1, len_y2, ((m-startX) + (m-ball[0]))**2]
            else:
                length = [len_y1, len_y2, (startX + ball[0])**2]
        else:
            length = [len_x1, len_x2, len_y1, len_y2]
        answer.append(min(length))
        
    return answer
