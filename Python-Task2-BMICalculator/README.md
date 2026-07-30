# BMI Calculator Pro (Task 2)

A desktop-based Body Mass Index (BMI) tracker and calculator built using Python's `CustomTkinter` UI framework, featuring data persistence via CSV files and visual progress tracking using `matplotlib`.

---

## Tech Stack
- **Language**: Python 3.x
- **GUI Framework**: `customtkinter`
- **Data Visualization**: `matplotlib`
- **Data Storage**: `csv` (local flat-file database)
- **Utilities**: `os`, `tkinter` (messagebox)

---

## Key Features
- **Modern Graphical User Interface**: Styled with custom frames, responsive layouts, and a clean modern aesthetic via CustomTkinter.
- **Automated BMI Calculation**: Computes BMI dynamically from user-input weight (kg) and height (cm) with real-time category classification (Underweight, Healthy, Overweight, Obese).
- **Persistent Data Tracking**: Automatically logs records (Name, Weight, Height, BMI, and Category) into a local `bmi_records.csv` file.
- **Historical Trend Visualizer**: Generates dynamic line charts via `matplotlib` to track a user's BMI progress across multiple entries.
- **Input Validation & Error Handling**: Comprehensive error messages for missing fields, zero/negative values, or incorrect data types.

---

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LavanyaTrivedi25/OIRSIP.git
   cd Python-Task2-BMICalculator
