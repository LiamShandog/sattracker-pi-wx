# sattracker-pi-wx

**SatTracker Pi WX** is a Raspberry Pi-powered robotic ground station that tracks real low Earth orbit (LEO) weather satellites, receives their Automatic Picture Transmission (APT) signals, decodes raw weather images, and combines them with live regional weather forecasts — all in one integrated, open-source system.

---

## 🌐 Project Purpose

This project demonstrates how to combine:
- **Orbital tracking** using TLE data
- **Servo-driven pan/tilt control** for directional antennas
- **Software-defined radio (SDR)** signal reception
- **Live weather image decoding**
- **OpenWeatherMap API integration**
  
The system turns raw space-based radio signals into a useful, local weather forecasting tool — all built with accessible components and Python.

---

## 🧰 Hardware Requirements

| Component | Purpose |
|----------|---------|
| 🧠 Raspberry Pi 5 | Main control computer |
| 📡 RTL-SDR USB Dongle | To receive 137 MHz satellite APT signals |
| ⚙️ 2x SG90/MG90S Servos | Control azimuth + elevation of antenna mount |
| 🛰️ V-Dipole or QFH Antenna | For NOAA satellite reception |
| 🖨️ 3D Printed Pan-Tilt Base | Optional, STL included in `/stl/` folder |
| 🔌 5V external power supply | To safely power servos |

---

## 💻 Software Requirements

Install dependencies:
```bash
pip install -r requirements.txt
