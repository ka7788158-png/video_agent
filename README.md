<div align="center">

# 🎥 AI Video Assistant With RAG

**An intelligent multi-modal assistant for video transcription, summarization, and question-answering using Retrieval-Augmented Generation.**

</div>

---

## 📑 Table of Contents
- [✨ Overview](#-overview)
- [🚀 Features](#-features)
- [🏗️ Tech Stack](#️-tech-stack)
- [📦 Installation](#-installation)
- [💻 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📞 Contact](#-contact)

---

## ✨ Overview

This project is an AI-powered Video Assistant designed to deeply process and analyze video content. Whether you are providing a YouTube link, a Zoom/Google Meet recording, or directly uploading an MP4 file, this application seamlessly extracts the audio and generates a highly accurate transcription.

Beyond simple transcription, the system utilizes a **Retrieval-Augmented Generation (RAG)** architecture. By intelligently chunking the text, creating high-quality embeddings, and storing them in a vector database, it enables a dynamic chat interface. You can ask specific questions about the video content and receive instant, context-aware answers without needing to watch the entire footage.

---

## 🚀 Features

- **Multi-Source Video Input:** Natively supports YouTube URLs, MP4 file uploads, and virtual meeting recordings.
- **Accurate Transcription:** Utilizes robust models like Whisper (with Sarvam integration for regional languages such as Hindi) to transcribe audio.
- **Automated Summarization:** Instantly processes transcripts to generate comprehensive video summaries, key takeaways, and potential questions.
- **Interactive Q&A (RAG):** Chat directly with your video! The RAG pipeline ensures precise answers are retrieved directly from the video's context using vector stores and retrievers.
- **Cost-Effective & Open Integration:** Built entirely with accessible Python frameworks for local or cloud deployment.

---

## 🏗️ Tech Stack

- **Language:** Python
- **Audio Processing:** Whisper, Sarvam
- **AI & RAG Architecture:** Vector Stores, Embeddings, Text Chunking, Retrievers

---

## 📦 Installation

Ensure you have **Python 3.10+** installed on your system.

1. **Clone the repository**
   ```bash
   git clone https://github.com/ka7788158-png/video_agent.git
   cd video_agent
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

*(Note: Depending on your operating system, you may also need to install `ffmpeg` globally for seamless audio/video extraction.)*

---

## 💻 Usage

Once your environment is set up and any necessary API keys are configured, launch the main application. 

Upload your target video file or paste a supported video link into the interface to initiate the transcription and embedding process. Once the vector store is fully populated, you can utilize the chat interface to query the video, ask for summaries, or extract specific data points.

---

## 🤝 Contributing

Contributions are highly encouraged! If you'd like to improve the tool, add new features, or optimize the RAG pipeline:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📞 Contact

**Developer:** Kavya Agrawal  
**Project Link:** [https://github.com/ka7788158-png/video_agent](https://github.com/ka7788158-png/video_agent)
