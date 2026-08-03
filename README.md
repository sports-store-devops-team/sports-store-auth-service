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

## Continuous integration

Pull requests targeting `main` run the pytest suite and a non-publishing container build. Pushes to `main` repeat validation, authenticate to AWS through GitHub OIDC, and publish exactly one immutable ECR image tagged `<VERSION>-<7-character-git-hash>`. `VERSION` is the semantic-version source and changes are made deliberately through a pull request.

Configure the Actions variables `AWS_REGION` and `AWS_ECR_PUBLISH_ROLE_ARN` at repository or organization scope. The role ARN is configuration, not a secret; no static AWS credentials are stored. CI does not deploy to EKS. Deployment is handled later through Argo CD.
