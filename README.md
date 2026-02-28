# Ai-ChatBot-with-Gemini

A premium Streamlit web application that lets you chat with Google Gemini (Generative AI). Experience a seamless, conversational interface powered by Google's latest Generative AI models.

## Features

- **Interactive Chat**: Engage in real-time dialogue with Gemini-Pro.
- **Modern UI**: A sleek, responsive design using Streamlit and custom CSS.
- **Customizable**: Adjust parameters and model settings via the sidebar.
- **Safe & Secure**: Uses environment variables for API key management.

## Getting Started

Follow these steps to set up and run the chatbot on your local machine.

### Prerequisites

- Python 3.9+
- A Google Gemini API key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aksaqi313/Ai-ChatBot-with-Gemini.git
   cd Ai-ChatBot-with-Gemini
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and add your Google API Key:
   ```bash
   GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY_HERE
   ```
   You can generate an API key at [Google AI Studio](https://aistudio.google.com/apikey).

### Running the App

Start the Streamlit server:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

## Usage

1. Enter your message in the chat input box at the bottom.
2. Use the sidebar to adjust model settings (if available).
3. Experience real-time responses from Gemini.

## Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---
Developed with ❤️ by [Azhar Khan](https://github.com/aksaqi313)
