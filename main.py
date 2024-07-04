import cv2
import mediapipe as mp
import serial

#conexão serial
ser = serial.Serial(
    port='COM6',       # door
    baudrate=9600,    
    timeout=1          
)

# Configurações da biblioteca
video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)

# Variável responsável pelos pontos da mão
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                pontos.append((cx, cy))

        dedos = [8, 12, 16, 20]
        cont = 0
        if points:
            # Lógica do dedão
            if pontos[4][0] < pontos[2][0]:
                cont += 1
            # Demais dedos
            for x in dedos:
                if pontos[x][1] < pontos[x - 2][1]:
                    cont += 1

        cv2.putText(img, str(cont), (400, 200), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 5)
        cv2.putText(img, str("press 'c' to leave"), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        serialCommand = f'{cont}\r\n'
        ser.write(serialCommand.encode('utf-8'))

    #caso não encontre nenhuma mão, desligue os leds
    else:
        serialCommand = '0'
        ser.write(serialCommand.encode('utf-8'))

    cv2.imshow("Imagem", img)
    
    # Captura a tecla pressionada
    key = cv2.waitKey(1)
    
    # o programa é fechado com a tecla "c"
    if key & 0xFF == ord('c'):
        break

# Libera a captura de vídeo e destrói todas as janelas
video.release()
cv2.destroyAllWindows()
ser.close()
