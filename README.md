### KFC-Genie-The-Ultimate-Voice-Assistant
### Development Plan for Drive-In Assistant

#### Project Overview
The Drive-In Assistant will accept and process food orders using voice commands, interface with a KFC menu API, confirm orders verbally, calculate costs, and suggest meal combos. The system will leverage open-source LLMs (e.g., LLAMA, Mistral, ChatGPT) for natural language processing and Google’s speech recognition for voice input.

#### Tools and Technologies
- **Language Models**: LLAMA, Mistral, ChatGPT
- **API Development**: Flask (preferred), Django, FastAPI
- **Voice Recognition**: Google Speech Recognition, noise reduction with spectral gating
- **Text-to-Speech**: speech T5 model, pyttsx3

#### System Requirements
1. **Voice Recognition**: Capture voice commands in noisy environments.
2. **API Development**: Robust API to connect AI with KFC menu data.
3. **Order Confirmation**: Verbal confirmation of order specifics and total cost.
4. **Upselling Capability**: Suggest premium meal options or add-ons.
5. **User Interface**: Support voice input, menu navigation, and receipt viewing.

#### Expected Deliverables
1. **Functionality**: Accurate voice-to-text conversion and real-time menu integration.
2. **User Interface**: Intuitive interface for order information and user interactions.
3. **Documentation**: Detailed documentation on API integration, system architecture, LLM implementation, and user interaction workflow.
4. **Presentation**: Demonstration simulating typical order scenarios.

#### Evaluation Criteria
1. **Accuracy**: Precision in voice command interpretation and order accuracy.
2. **Responsiveness**: Efficiency in command processing and API interaction.
3. **User Experience**: Interface effectiveness and streamlined ordering process.
4. **Innovation**: Creative application of technology in system features.

#### Implementation Steps
1. **Environment Setup**
    - Set up the development environment.
    - Install required libraries and frameworks (Flask, LangChain, Google Speech Recognition, etc.).

2. **API Development**
    - Create a Flask API to interface with the KFC menu data stored in a CSV file.
    - Implement endpoints for fetching menu items, processing orders, and calculating total costs.

3. **Voice Recognition and Noise Reduction**
    - Integrate Google Speech Recognition for capturing voice commands.
    - Implement noise reduction using spectral gating to enhance voice command accuracy in noisy environments.

4. **Natural Language Processing**
    - Use LangChain to integrate with open-source LLMs (LLAMA, Mistral, ChatGPT) for processing voice-to-text inputs.
    - Load KFC menu data into the LLM for query responses.

5. **Text-to-Speech (TTS)**
    - Use the speech T5 model for natural voice responses.
    - Integrate pyttsx3 as a fallback TTS solution.

6. **Frontend Development**
    - Create a login page for customer details using HTML and Flask.
    - Develop a menu page displaying items from the API and supporting voice input.
    - Add a microphone button for capturing voice commands.

7. **Order Confirmation and Upselling**
    - Implement verbal order confirmation and cost calculation.
    - Integrate a recommendation engine for suggesting premium meal options based on promotions or preferences.

8. **Testing and Validation**
    - Test the system for accuracy in voice recognition, order processing, and TTS responses.
    - Validate the API and frontend integration for seamless interaction.

9. **Documentation and Presentation**
    - Prepare comprehensive documentation covering API integration, system architecture, and user workflow.
    - Create a demonstration to simulate typical drive-through order scenarios.

#### How to Use the Model
1. **Setup**
    - Download the `requirements.txt` file.
    - Run `app.py` in the backend.
    - Run `customer_details.html` in the frontend.

2. **Login**
    - Fill in user credentials on the login page.
    - Access the menu page upon successful login.

3. **Voice Ordering**
    - Click the microphone button on the menu page to start recording the order.
    - Repeat for additional items if necessary.

By following these steps, the Drive-In Assistant will provide an efficient and user-friendly ordering experience at KFC drive-throughs.




### Text-to-Speech (TTS) using SpeechT5 with HiFi-GAN Vocoder
This Python script demonstrates a Text-to-Speech (TTS) system using the SpeechT5 model from Hugging Face's Transformers library. It loads the model and vocoder, processes text input, generates speech, and saves the output to a WAV file. The script uses logging to track module loading and model loading times for performance monitoring.

## Key Components:
- Module Loading: Imports necessary libraries (torch, soundfile, transformers, datasets) and logs the time taken for module importation.
- Model Loading: Loads the SpeechT5 model and HiFi-GAN vocoder from the Hugging Face model hub, logging the time taken for model initialization.
- Text Processing: Converts input text into speech using the loaded model and vocoder.
- Logging: Utilizes logging to record detailed information about module loading, model loading, and speech generation processes.

## Dependencies:
- torch: PyTorch library for tensor computations.
- soundfile: Library for reading and writing sound files.
- transformers: Hugging Face's library for NLP and deep learning.
- datasets: Hugging Face's library for accessing and managing datasets.

## Usage:
- **Install Dependencies:** Ensure dependencies are installed by running the following command:
```
pip install -r requirements.txt
```
- **Python Version:** This script is compatible with Python version 3.8.10.
- **Run Script:** Execute the script to record, preprocess, and transcribe audio:
```
python TTS.py
```
- **Logging Setup:** Configure logging to tts_log.txt file with timestamps (%(asctime)s), log levels (%(levelname)s), and detailed messages (%(message)s).
- **Run Script:** Execute the script (python script.py) to generate speech from the provided text input and save it as speech.wav.

This script provides a streamlined approach to convert text into speech using state-of-the-art neural network models, offering flexibility for various TTS applications.



# Speech-to-Text (STT) with Noise Reduction

This Python script demonstrates a Speech-to-Text (STT) system using the speech_recognition library combined with noise reduction techniques using noisereduce. It records audio from the microphone, reduces noise, and transcribes speech into text using Google's Speech Recognition API. Audio preprocessing includes noise reduction and volume normalization for improved accuracy.

## Key Features:
- Records audio from microphone using speech_recognition.
- Applies noise reduction using noisereduce.
- Normalizes volume to maintain voice consistency.
- Transcribes speech to text using Google's Speech Recognition API.

## Dependencies:
- speech_recognition
- noisereduce
- numpy
- pydub

## Usage:
- **Install Dependencies:** Ensure dependencies are installed by running the following command:
```
pip install -r requirements.txt
```
- **Python Version:** This script is compatible with Python version 3.8.10.
- **Run Script:** Execute the script to record, preprocess, and transcribe audio
```
python STT.py
```
