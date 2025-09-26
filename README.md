# 📬 Notification Service

Event-driven notification system in Python supporting multi-channel delivery (Email, SMS, Push) with retries, queues, and observability.  
Built to scale and easy to extend.

---

## 🚀 Quick Start

```bash
# clone repo
git clone https://github.com/your-username/notification-service.git
cd notification-service

# start services
docker-compose up --build

📖 API Endpoints

Health Check
GET /health

Send Notification
POST /notifications/

{
  "tenant_id": "t1",
  "user_id": "u1",
  "channel_id": "email",
  "message": "Hello FAANG"
}

📂 Repository Structure

notification-service/
├── docs/                # architecture diagrams, scaling notes
├── src/
│   ├── api/             # FastAPI endpoints
│   ├── workers/         # queue consumers
│   ├── services/        # email, SMS, push adapters
│   ├── models/          # DB schemas
│   └── utils/           # logging, error handling
├── tests/               # pytest unit & integration tests
├── docker/              # Dockerfiles, compose setup
├── helm/                # (optional) K8s manifests
├── .github/workflows/   # CI/CD pipelines
└── README.md

📜 License
Apache 2.0