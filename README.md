
# 🚀 Internly – Intelligent Job & Internship Finder

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white" alt="Railway">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-Learn">
</p>

**Internly** is a full-stack Job & Internship Intelligence System that aggregates opportunities from multiple platforms and ranks them using NLP-based relevance scoring. It helps students and early professionals discover the most relevant roles faster, without manually browsing multiple job portals.

> **Search once. Discover smarter.**

---

## 📑 Table of Contents
- [🌐 Live Demo](#-live-demo)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🧠 System Architecture](#-system-architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Local Setup](#️-local-setup)
- [🧪 API Usage](#-api-usage)
- [👤 Authors](#-authors)

---

## 🌐 Live Demo

- **Backend API (FastAPI):** [https://your-railway-domain.up.railway.app](https://your-railway-domain.up.railway.app)
- **Example Endpoint:** `GET /search?role=python`

---

## ✨ Features

- 🔎 **Smart Job Search:** Search by role (e.g., Python Developer, Web Development, Data Science).
- 🧠 **NLP Relevance Scoring:** Jobs are ranked using **TF-IDF + Cosine Similarity**.
- 🌐 **Multi-Source Aggregation:** Currently supports **Internshala** (designed for easy expansion).
- 🕒 **Human-Readable Timing:** Displays results like “Posted 2 days ago”.
- 🎨 **Modern Dark UI:** Card-based grid layout inspired by modern platforms.
- 🚀 **Production Ready:** Dockerized and deployed on Railway with dynamic port handling.

---

## 🛠️ Tech Stack

| Component | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3.10, FastAPI, Uvicorn, BeautifulSoup4 |
| **NLP** | Scikit-learn (TF-IDF), NumPy |
| **Frontend** | HTML5, CSS3 (Dark Theme), Vanilla JavaScript |
| **DevOps** | Docker, Railway, Git & GitHub |
| **Database** | SQLAlchemy (Ready for persistence) |

---

## 📁 Project Structure
Internly/
├── backend/
│   ├── main.py          # FastAPI app entry point
│   ├── scraper.py       # Job scraping logic
│   ├── nlp_engine.py    # NLP relevance scoring
│   ├── models.py        # Data models
│   └── database.py      # DB setup (optional)
├── frontend/
│   └── index.html       # UI interface
├── Dockerfile           # Production container setup
├── requirements.txt     # Dependency list
└── README.md            # Project documentation
⚙️ Local Setup

Clone the repository

git clone https://github.com/your-username/Internly.git
cd Internly

Install dependencies:
pip install -r requirements.txt

Run the backend:
uvicorn backend.main:app --reload

The API will be live at http://127.0.0.1:8000


🔮 Future Enhancements

Job Alerts: Receive email and push notifications for new matches.

Skill Gap Analysis: Suggestions for skills needed for specific roles.

Resume Job Matching: Upload your resume to receive a matching score.

Extended Sources: Integration with LinkedIn, Indeed, and Wellfound.

👤 Authors
Name	Role	Socials
Sreehari Vinod	Lead Developer	
![alt text](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)
![alt text](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)

Rooney Francis	UI/UX Designer	
![alt text](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)
![alt text](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)
⭐ Final Note

This project is built with real-world deployment constraints. Every feature—from scraping limits to NLP trade-offs—reflects practical engineering decisions.

If you’re reviewing this project: Run it. Break it. Improve it. 🚀
