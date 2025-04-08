import cv2
import mediapipe as mp
import serial
import time

# Configurar el puerto serial (ajusta COMx según tu sistema)
ser = serial.Serial('COM6', 9600)
time.sleep(2)

# Inicializar MediaPipe manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Inicializar cámara
cap = cv2.VideoCapture("http://192.168.100.9:4747/video")

prev_x = None
threshold = 40  # Umbral de movimiento en píxeles

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Espejo para comodidad
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar los landmarks en la imagen
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Coordenadas del landmark 0 (base de la palma)
            h, w, _ = frame.shape
            x = int(hand_landmarks.landmark[0].x * w)

            # Comparar posición con el frame anterior
            if prev_x is not None:
                dx = x - prev_x
                if dx > threshold:
                    print("Derecha")
                    ser.write(b'1e')
                    time.sleep(0.5)
                elif dx < -threshold:
                    print("Izquierda")
                    ser.write(b'6e')
                    time.sleep(0.5)

            prev_x = x

    # Mostrar cámara
    cv2.imshow("Hand Tracking", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpiar
cap.release()
cv2.destroyAllWindows()
ser.close()
