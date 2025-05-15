import streamlit as st
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Carrega o modelo
model = YOLO("models/best.pt")

st.title("Deteção de EPI")
st.markdown("Faça upload de uma imagem ou vídeo para verificar a presença de equipamentos de proteção individual (EPI).")

# Seletor entre imagem e vídeo
tipo_input = st.radio("Seleciona o tipo de ficheiro", ["Imagem", "Vídeo"])

# Classes (para referência futura)
CLASSES = ['Dust Mask', 'Eye Wear', 'Glove', 'Protective Boots', 'Protective Helmet', 'Safety Vest', 'Shield']

if tipo_input == "Imagem":
    uploaded_file = st.file_uploader("Faz upload de uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        results = model(image, conf=0.2)[0]
        annotated = results.plot()

        # Extrai classes detetadas
        labels = [CLASSES[int(cls)] for cls in results.boxes.cls]

        def calcular_conformidade(labels):
            total_pessoas = labels.count("Protective Helmet")
            if total_pessoas == 0:
                return 0
            conformes = 0
            for cls in ['Protective Helmet', 'Safety Vest']:
                conformes += labels.count(cls)
            taxa = int((conformes / (2 * total_pessoas)) * 100)
            return taxa

        taxa = calcular_conformidade(labels)

        st.image(annotated, channels="BGR", caption="Imagem com deteções")
        st.write("**EPIs Detetados:**", labels)
        st.metric("✅ Taxa de Conformidade", f"{taxa}%")

elif tipo_input == "Vídeo":
    uploaded_video = st.file_uploader("Faz upload de um vídeo", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        # Guarda o vídeo temporariamente
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        st.info("A processar vídeo... Pressiona ESC para parar.")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Corre deteção
            results = model(frame, conf=0.3)[0]
            annotated = results.plot()

            # Converte para RGB para Streamlit
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            stframe.image(annotated_rgb, channels="RGB", use_column_width=True)

        cap.release()
        st.success("✅ Vídeo processado com sucesso.")
