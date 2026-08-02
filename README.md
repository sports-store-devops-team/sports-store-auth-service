# Sports Store Auth Service

FastAPI service for user registration, login, JWT issuance, and user identity. It listens on port `8001`; health is available at `GET /health`.

## Configuration

| Variable | Required | Purpose |
| --- | --- | --- |
| `MONGO_URI` | Yes | MongoDB connection URI for the auth database. |
| `JWT_SECRET` | Yes | Shared signing secret; use a secure value outside development. |
| `JWT_ALGORITHM` | No | JWT algorithm (default `HS256`). |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | No | Token lifetime (default `60`). |

`.env.example` contains development-only placeholders. Do not use them in production.

## Build and test

```sh
docker build -t sports-store/auth-service:0.1.0 .
python -m pytest
```

Run locally with `uvicorn main:app --host 0.0.0.0 --port 8001` after providing the required environment variables.
