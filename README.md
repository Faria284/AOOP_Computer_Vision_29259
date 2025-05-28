# Sistema de Deteção de Equipamento de Proteção Individual (EPI)

Este projeto aplica **Computer Vision** com **YOLOv8** para detetar automaticamente Equipamento de Proteção Individual (EPI) - como capacetes, coletes, máscaras e óculos - em imagens e vídeos de ambientes industriais. Inclui também um **dashboard interativo em Streamlit** com visualização e análise de conformidade.

---

## Objetivo

Desenvolver um sistema simples e funcional que:
- Identifique se os trabalhadores estão a usar os EPIs obrigatórios.
- Apresente os resultados de forma visual intuitiva.
- Seja facilmente aplicável em contexto industrial ou académico.

---

## Tecnologias Utilizadas

- **Python 3.11**
- [YOLOv8 - Ultralytics](https://github.com/ultralytics/ultralytics)
- OpenCV
- Streamlit
- NumPy / Pillow
- (Opcional) Pandas

---

## Instalação

1. Clona ou descarrega este repositório.
2. Instala as dependências:
```bash
pip install -r requirements.txt
```

---

## Executar o dashboard

1. Através do terminal executa o seguinte comando:
```bash
streamlit run dashboard/app.py
```

---

## Dataset

Utilizado um dataset público da Roboflow (https://universe.roboflow.com/project-uyrxf/ppe_detection-v1x3l/dataset/2) com as seguintes classes:
- Dust Mask
- Eye Wear
- Glove
- Protection Boots
- Protection Helmet
- Safety Vest
- Shield

---

## Resultados do Treino

Treinado com YOLOv8n por 20 épocas em CPU:
- **mAP@0.5:**0.883
- **mAP@0.5:0.95:**0.598

## Funcionalidades

**Deteção em Imagem**
- Upload de imagens via dashboard
- Visualização com bounding boxes
- Contagem de classes
- Cálculo da taxa de conformidade (% de EPIs por pessoa).

**Deteção em Vídeo**
- Upload de vídeo via dashboard
- Processamento frame a frame
- Anotação ao vivo

---

## Autor
**Diogo Fernandes Faria Nº29259**
Projeto académico para a Unidade Curricular de Aprendizagem Organizacional do 3ºano do curso de Engenharia Informática do Instituto Politécnico de Viana do Castelo.

---

## Licença
Este projeto foi desenvolvido apenas para fins académicos. Dataset original disponível sob a licença CC BY 4.0 na Roboflow.