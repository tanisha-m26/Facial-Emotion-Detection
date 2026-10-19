# Facial Emotion Detection Setup Guide

Follow these sequential steps to install the environment and execute the project from scratch.

### Step 1: Pre-requisites & Terminal Initialization
# [CRITICAL SYSTEM PRE-REQUISITE]: 
# Download and install Miniconda (recommended over heavy Anaconda to save ~4GB of storage space)
# installer from the official website: https://anaconda.com
# Make sure to check the box "Add Miniconda to my PATH environment variable" during installation.

# Open Git Bash and initialize the shell for conda tracking:
conda init bash

# Close Git Bash and open a fresh Git Bash terminal window to load the profile paths.

### Step 2: Isolated Environment Setup
# Create a lightweight Python environment optimized for deep learning stability
conda create -n facial python=3.10 -y

# Activate the sandbox workspace
conda activate facial

### Step 3: Efficient Dependency Installation
# Install exact compatible packages directly through your requirements profile
pip install ultralytics
pip install -r requirements.txt

### Step 4: Hardware Check & Verification
# Verify Windows Privacy Settings -> Camera -> "Allow desktop apps to access your camera" is enabled.
# Close external apps using your webcam (Zoom, Teams, Discord) to avoid hardware lockups.

### Step 5: Execute Application
python main.py

---

## Project Overview
This repository hosts a real-time computer vision workflow utilizing **YOLOv11** optimized to run facial emotion expressions parsing via a dynamic frame inference stream. By utilizing **Miniconda runtime containers** alongside an explicit dependency profile constraint, the environment stays tightly isolated beneath a sub-40ms loop delay footprint, bypassing heavy architectural frameworks to comfortably process active predictions directly inside edge devices.
