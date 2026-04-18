
***

# EC Prep 📚

An AI-powered web application built with Python and Streamlit to help students summarize notes and generate practice quizzes from PDF materials.

## 🚀 Getting Started

Follow these steps exactly to set up the project on your machine.

### 1. Prerequisites
Ensure you have Python 3 and the `venv` module installed. Open your terminal and run:
```bash
sudo apt update
sudo apt install python3-pip python3-venv python3-full -y
```

### 2. Project Setup
Create a dedicated folder for the project and move into it:
```bash
mkdir studyMate
cd studyMate
```

### 3. Create a Virtual Environment
To avoid "Externally Managed Environment" errors, we use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
*Note: You should now see `(venv)` at the start of your terminal prompt.*

### 4. Install Dependencies
Install the required Python libraries inside the virtual environment:
```bash
pip install streamlit google-generativeai python-dotenv PyPDF2
```

### 5. Configure API Keys
You must have a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

1. Create a file named `.env` in the root folder:
   ```bash
   touch .env
   ```
2. Open the `.env` file and paste your key:
   ```text
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 6. Create the Application File
Create a file named `app.py` and paste the "Fully Corrected" code provided in our conversation. 

**Important:** Ensure the model line uses the version confirmed by your system:
```python
model = genai.GenerativeModel('gemini-2.5-flash')
```

---

## 💻 How to Run
Every time you want to use the app, follow these two steps:

1. **Activate the Environment:**
   ```bash
   source venv/bin/activate
   ```
2. **Launch Streamlit:**
   ```bash
   streamlit run app.py
   ```
The app will automatically open in your default web browser (usually at `http://localhost:8501`).

---

## 🛠️ Troubleshooting

| Error | Solution |
| :--- | :--- |
| **404 Model Not Found** | Ensure `app.py` uses `gemini-2.5-flash`. Run the diagnostic script to check available models. |
| **Externally Managed Environment** | You forgot to activate the virtual environment. Run `source venv/bin/activate`. |
| **Blank Page in Browser** | Refresh the page (Ctrl+Shift+R) or check the terminal for Python errors. |
| **API Key Missing** | Ensure your `.env` file is named exactly that and is in the same folder as `app.py`. |

---

