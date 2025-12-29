<!-- PROJECT LABELS -->
![status](https://img.shields.io/badge/status-stable-brightgreen)
![type](https://img.shields.io/badge/type-BLE%20Daemon-blue)
![platform](https://img.shields.io/badge/platform-Termux%20%7C%20Android-lightgrey)
![language](https://img.shields.io/badge/language-Python-green)
![license](https://img.shields.io/badge/license-MIT-black)
# Buzit BLE Daemon



# Buzit BLE Daemon

Canonical Core – v1.0.0

A Termux-based Bluetooth Low Energy (BLE) daemon for reliably triggering and controlling BLE devices using mic events, REST calls, or CLI, designed to run continuously as a background service.

Buzit BLE Daemon is a Termux-based Bluetooth Low Energy (BLE) daemon designed to
reliably trigger and control BLE devices using mic events, REST calls, or CLI
commands. It runs continuously as a background service and is suitable for
automation, experimentation, and controlled device signaling.

---

## Features

- BLE device discovery, connection, and write control
- Optional mic-based trigger input
- REST API trigger (FastAPI)
- Dry-run mode for safe testing
- Structured logging (JSON logs)
- Termux-compatible daemon wrapper
- Minimal, auditable core logic

---

## Architecture Overview

High-level flow:



# Buzit BLE Daemon

Buzit BLE Daemon is a Termux-based Bluetooth Low Energy (BLE) daemon that syncs devices using mic triggers and remote HTTP control.

## Features
- BLE device management
- Mic-based buzz triggers
- Remote HTTP control
- Lightweight and efficient

## Installation
Clone the repository:
```
git clone https://github.com/figuripv6o/buzit_ble_daemon.git
cd buzit_ble_daemon
```

## Usage
Run the daemon with:
```
python3 buzit_daemon.py
```

## Author
Built with passion by **Buzzo**.
