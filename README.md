# Dynamic 5G Bandwidth Allocation using FastAPI, MongoDB & GNU Radio

## Overview
This project implements a **Dynamic 5G Bandwidth Allocation backend** that acts as a bridge between a **Traffic Generator / ML-based allocation logic** and **GNU Radio**.

The backend:
- Receives bandwidth allocation data
- Stores it in MongoDB
- Fetches and processes stored data
- Converts it into a **binary (.bin) file**
- Makes it ready for **GNU Radio consumption**

This repository contains **only the FastAPI backend**.

---

## System Architecture & Data Flow

Traffic Generator / ML Model
|
| (JSON allocation data)
v
FastAPI Backend (this repo)
|
|--> Stores data in MongoDB
|
|--> Fetches & processes stored data
|
|--> Converts data to binary (.bin)
v
Binary File (.bin)
|
v
GNU Radio Flowgraph


---

## Tech Stack

- **FastAPI** – REST backend
- **MongoDB** – Data storage
- **Python** – Processing & binary generation
- **GNU Radio** – Wireless simulation (external)

---

## Project Structure

backend/
│
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── config.py # MongoDB configuration
│ │
│ ├── api/
│ │ ├── init.py
│ │ └── sample.py # API routes
│ │
│ ├── database/
│ │ ├── init.py
│ │ ├── mongo.py # MongoDB connection
│ │ └── schemas.py # Pydantic models
│ │
│ ├── traffic/
│ │ └── traffic_generator.py
│
├── requirements.txt
└── README.md


---
