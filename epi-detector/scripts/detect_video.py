import cv2
from ultralytics import YOLO
import os

# Pede o caminho para o vídeo
video_path = input("Insere o caminho para o vídeo (ou 0 para webcam): ").strip()

# Verifica se é webcam
if video_path == "0":
    video_path = 0
elif not os.path.exists(video_path):
    print(f"Erro: O ficheiro '{video_path}' não existe.")
    exit(1)

# Carrega o modelo
model = YOLO("runs/detect/train3/weights/best.pt")

# Abre o vídeo
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Corre deteção com threshold de confiança
    results = model(frame, conf=0.2)[0]
    annotated = results.plot()

    # Mostra o frame com as deteções
    cv2.imshow("Deteção de EPI - Vídeo", annotated)

    # Sair ao premir Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
