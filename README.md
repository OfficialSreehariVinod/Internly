# 🚀 Internly – Intelligent Job & Internship Finder
Internly is a full-stack Job & Internship Intelligence System that aggregates opportunities from multiple platforms and ranks them using NLP-based relevance scoring.
It helps students and early professionals discover the most relevant roles faster, without manually browsing multiple job portals.

🔍 **Search once. Discover smarter.**

🌐 Live Demo

  Backend API (FastAPI)
    👉 https://your-railway-domain.up.railway.app

  Example Endpoint
    GET /search?role=python

✨ Features

🔎 Smart Job Search
  Search by role (e.g., Python Developer, Web Development, Data Science)

🧠 NLP-Based Relevance Scoring
  Jobs are ranked using TF-IDF + cosine similarity

🌐 Multi-Source Aggregation
  Currently supports:

Internshala
  (architecture supports easy extension to other portals)

🕒 Human-Readable Posting Time
    Displays results like “Posted 2 days ago”

🎨 Modern Dark UI
    Card-based grid layout inspired by modern job platforms

🚀 Production Deployment
    Dockerized & deployed on Railway

🏗️ Tech Stack
  Backend
  Python 3.10
  FastAPI
  Uvicorn
  BeautifulSoup4 – Web scraping
  scikit-learn – NLP similarity
  NumPy
  SQLAlchemy (ready for persistence)
  Frontend
  HTML5
  CSS3 (Dark Theme UI)
  Vanilla JavaScript (Fetch API)
  DevOps
  Docker
  Railway (Cloud Deployment)
  Git & GitHub

🧠 System Architecture

  
  User Search Query
          ↓
  Keyword Normalization
          ↓
  Job Scraper (Internshala)
          ↓
  NLP Similarity Engine
          ↓
  Relevance Scoring
          ↓
  Ranked Results API
          ↓
  Frontend Card UI

📁 Project Structure
  Internly/
  ├── backend/
  │   ├── main.py          # FastAPI app
  │   ├── scraper.py       # Job scraping logic
  │   ├── nlp_engine.py    # NLP relevance scoring
  │   ├── models.py        # Data models
  │   └── database.py      # DB setup (optional)
  │
  ├── frontend/
  │   ├── index.html      
  │
  ├── Dockerfile
  ├── requirements.txt
  └── README.md

⚙️ Local Setup
  1️⃣ Clone the repository
    git clone https://github.com/your-username/Internly.git
    cd Internly

  2️⃣ Install dependencies
    pip install -r requirements.txt

  3️⃣ Run the backend
    uvicorn backend.main:app --reload

  Backend runs at:
    http://127.0.0.1:8000

🐳 Docker Setup (Production)
  docker build -t internly .
  docker run -p 8080:8080 internly

🚀 Deployment
  The backend is deployed using Docker on Railway, with dynamic port handling via environment variables.
  Key deployment learnings:
  Proper $PORT expansion using sh -c
  Python version compatibility
  Dependency pinning to avoid NumPy 2.x build issues
  Clean separation of frontend & backend

🧪 Sample API Response
[
  {
    "title": "Python Development Intern",
    "company": "Winfrox",
    "source": "Internshala",
    "posted": "Posted 2 days ago",
    "score": 0.41,
    "url": "https://internshala.com/..."
  }
]

📌 What I Learned
  Building real-world web scrapers
  Applying NLP for semantic relevance
  Designing REST APIs with FastAPI
  Debugging production Docker deployments
  Handling cloud platform quirks (Railway, Render)
  Writing clean, maintainable project structure

🔮 Future Enhancements

  🔔 Job alerts & notifications

  📊 Skill gap analysis

  🧾 Resume–Job matching

  🌍 More job portals

  🔐 User accounts & saved searches

  👤 Author

Sreehari Vinod
Computer Science Student | Python Developer | ML & Full-Stack Enthusiast | Full-Stack Developer | UI Designer

GitHub: https://github.com/OfficialSreehariVinod
LinkedIn: https://linkedin.com/in/sreeharivinodofficial

Rooney Francis
Computer Science Student | UI/UX Designer 

Wordpress: uiron.netlify.app
Github: https://github.com/iamRooney
LinkedIn: https://www.linkedin.com/in/rooney-francis/

⭐ Final Note

  This project is built with real deployment constraints, not just local demos.
  Every feature reflects practical engineering decisions — scraping limits, NLP tradeoffs, and production debugging.

If you’re reviewing this project:
👉 Run it. Break it. Improve it. That’s how it was designed.
