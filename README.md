# IoT Climate Chamber Project
**Author:** Teodorina Lungu  
**Course:** IoT Development - FITSTIC  
**Network IP:** 192.168.33.193

## 📖 Project Description
This repository contains a full-stack IoT solution for monitoring a seasoning climate chamber. The project demonstrates the transition from a basic Python monitoring script to a sophisticated microservices architecture using Docker and Node-RED.

---

## 📊 Presentation Overview (Ref: VerificaIoT.pdf)

### Slide 1: Python & MQTTool Phase
* **Concept:** Initial logic validation.
* **Logic:** Script `main_iot.py` processes temperature ranges:
    * 0-10°C: **Safe**
    * 10-20°C: **Warning**
    * 20-50°C: **Alarm**
* **Evidence:** Page 1 of `VerificaIoT.pdf` shows the mobile app receiving data via the school broker.

### Slide 2: Node-RED Backend Flow
* **Logic (Q3):** A specialized **Logic Q3** switch node directs data to four distinct status levels.
* **Documentation:** Every "Text" node uses the internal **Description** section for clear metadata management.
* **Evidence:** Page 2 of `VerificaIoT.pdf`.

### Slide 3: Desktop Dashboard (GUI)
* **GUI (Q1):** Real-time synchronization between the "Set Temperature" slider and the "Chamber Temp" gauge.
* **Color Logic:** * **Green:** 0-10°C (L1 Active)
    * **Yellow:** 10-20°C (L2 Active)
    * **Orange Warning:** 20-30°C (Pre-alarm logic)
    * **Red:** 30-50°C (L3 Critical)
* **Evidence:** Page 3 of `VerificaIoT.pdf`.

### Slide 4: Mobile Remote Access
* **Connectivity (Q4/Q5):** The dashboard is fully responsive and accessible via mobile browser on the school network.
* **URL:** `http://192.168.33.193:1880/ui`
* **Evidence:** Page 4 of `VerificaIoT.pdf`.

---

## 🛠️ Technical Implementation
* **Docker:** Managed via `docker-compose.yml` for Mosquitto and Node-RED.
* **MQTT:** Used for bidirectional synchronization between the logic and the UI.
* **Logica Arancione:** Added an intermediate orange phase to provide higher granularity in the warning system.

## 🚀 How to Run
1. Clone the repo.
2. Run `docker-compose up -d`.
3. Open `http://localhost:1880/ui`.
