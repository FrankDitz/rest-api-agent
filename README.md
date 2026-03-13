# rest-api-agent
This project ingests agent data through a REST API, cleans and transforms the payload, stores the normalized result, and prepares it for downstream distribution to external APIs.

## Project Structure
agent-data-normalizer/
│
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── schemas.py        # request/response models
│   ├── transform.py      # cleaning + normalization logic
│   ├── database.py       # DB setup
│   ├── repository.py     # database queries
│   └── distributor.py    # downstream API sender
│
├── requirements.txt
└── README.md