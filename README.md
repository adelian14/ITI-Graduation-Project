
# 📘 ITI-Graduation-Project

## 🚀 Overview

This project transforms static PDF educational content into structured, interactive, and multimedia-rich lessons. By combining cutting-edge OCR, semantic understanding, vector embeddings, and autonomous agents powered by **CrewAI**, it enables automated content parsing, knowledge structuring, lesson creation, summarization, multimedia generation, and roadmapping.

---

## 🧠 Core Features

* 📄 **PDF Upload & Processing**

  * Upload any PDF file (e.g., textbooks, lecture notes).
  * Perform OCR (Optical Character Recognition) to extract text from scanned or image-based PDFs.

* 🧩 **Content Structuring**

  * Automatically split content into `Modules`, `Lessons`, and `Topics` using semantic segmentation.
  * Store the structured content in a vector database after embedding.

* 🔍 **Semantic Search & Lesson Retrieval**

  * Select a topic or lesson and retrieve **semantically related content** using vector similarity search.

* 🧑‍💼 **AI-Powered Agent Workflow (via CrewAI)**

  * **Agent 1:** Generate a complete lesson from the topic.
  * **Agent 2:** Summarize the lesson content.
  * **Agent 3:** Convert the summary into structured JSON format.
  * **Agent 4:** Create PowerPoint (PPTX) slides for the lesson.
  * **Agent 5:** Generate a narrative and video script for the lesson.

* 🗺️ **Roadmap Generation**

  * Convert the entire PDF into a **visual roadmap** showing module > lesson > topic hierarchy.

---

## 🛠️ Tech Stack & Tools

| Component        | Tool Used                                   | Why Chosen                                                                   |
| ---------------- | ------------------------------------------- | ---------------------------------------------------------------------------- |
| OCR              | `Tesseract` or similar                      | High accuracy and open-source                                                |
| LLM              | `Gemini-2.5-Flash`                          | Fast, efficient, suitable for real-time tasks                                |
| Embedding Model  | `BAAI/bge-base-en-v1.5`                     | Optimized for semantic search, high performance on sentence-level embeddings |
| Vector DB        | `Qdrant`                                    | Scalable, fast similarity search, supports filtering, production-ready       |
| Agents Framework | `CrewAI`                                    | Easy orchestration of autonomous agents, task-based execution                |
| Output Formats   | `JSON`, `PPTX`, `Narrative`, `Video Script` | Rich content formats for various educational needs                           |

---

## 🧩 How It Works

1. **PDF Upload & OCR**

   * User uploads a PDF.
   * OCR engine extracts text content (supports multi-page).

2. **Content Understanding & Segmentation**

   * LLM parses content into structured hierarchy (Modules > Lessons > Topics).
   * Text is embedded using BAAI/bge-base-en-v1.5 and stored in Qdrant.

3. **Semantic Search**

   * User selects a topic or lesson.
   * System retrieves related content using similarity search from Qdrant.

4. **Agent Pipeline Execution (CrewAI)**

   * **Agent 1:** Creates a detailed lesson.
   * **Agent 2:** Summarizes that lesson.
   * **Agent 3:** Converts into structured JSON.
   * **Agent 4:** Generates PPTX slides.
   * **Agent 5:** Creates narrative + video script.

5. **Roadmap Creation**

   * Use the parsed structure to generate a visual learning roadmap.

---

## 🔍 Advantages Over Alternatives

| Feature         | Our Stack                                   | Traditional Tools                         |
| --------------- | ------------------------------------------- | ----------------------------------------- |
| OCR             | Fast, high-accuracy, open-source            | Often locked behind APIs or low accuracy  |
| Embeddings      | BAAI/bge-base-en-v1.5 (State-of-the-art)    | General-purpose, less accurate embeddings |
| Vector DB       | Qdrant (filterable, scalable, blazing fast) | FAISS lacks filtering, Pinecone is costly |
| Agent Framework | CrewAI (modular, agent orchestration)       | Manual coding or brittle scripts          |
| LLM             | Gemini 2.5 Flash (speed + cost effective)   | Slower and expensive options like GPT-4   |
| Output Options  | JSON, PPTX, Narrative, Script               | Limited or manual conversion              |
| Semantic Search | Context-aware via vector similarity         | Basic keyword match                       |

---

## ✨ Use Cases

* Automating lesson design for teachers.
* Converting legacy content into interactive formats.
* Personalized learning through topic-based retrieval.
* Course material generation for e-learning platforms.

---

## 📦 Folder Structure

```
project/
├── uploads/               # Uploaded PDFs
├── ocr/                   # Extracted text
├── modules/               # Parsed structured content
├── agents/                # CrewAI agent definitions
├── embeddings/            # BAAI embeddings
├── pptx_outputs/          # Generated PowerPoints
├── narratives/            # Lesson narratives
├── scripts/               # Video scripts
├── roadmaps/              # Visual roadmaps
├── database/              # Qdrant or related configs
└── README.md              # This documentation
```

---

## 🧪 Example Workflow

1. **Upload PDF**
2. **Extracted Text:**

   ```
   Chapter 1: Introduction to AI
   - What is AI?
   - History of AI
   ```
3. **Module → Lesson → Topic:**

   * Module: "Intro to AI"

     * Lesson: "AI Basics"

       * Topic: "History of AI"
4. **Search Query:** "What is AI?"
5. **Agents Activated:**

   * Lesson → Summary → JSON → PPTX → Script

---

## 📌 Future Improvements

* 🎤 Text-to-speech and video generation.
* 🔒 User authentication and saved projects.
* 🗂️ Multiple file uploads and cross-referencing.

