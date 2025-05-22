import cv2
from ultralytics import YOLO
import os

# Pede ao utilizador o caminho para a imagem
image_path = input("Insere o caminho para a imagem: ").strip()

# Verifica se o ficheiro existe
if not os.path.exists(image_path):
    print(f"Erro: O ficheiro '{image_path}' não existe.")
    exit(1)

# Carrega o modelo treinado
model = YOLO("runs/detect/train3/weights/best.pt")

# Lê a imagem
img = cv2.imread(image_path)

# Corre a deteção
results = model(img, conf=0.2)[0]
annotated = results.plot()

# Mostra resultado
cv2.imshow("Deteção de EPI", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
