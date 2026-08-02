# Deployment Guide

## Prerequisites
- Docker & Docker Compose
- Node.js (for manual builds)
- Accounts on Vercel and Render (for cloud deployment)

---

## Option 1: Docker Deployment (Local & Server)

The easiest way to run the entire stack locally or on a standard VPS.

1.  Clone the repository and enter the directory.
2.  Start the stack:
    ```bash
    docker-compose up -d --build
    ```
3.  Verify the backend health:
    ```bash
    curl http://localhost:8000/api/v1/health
    ```
4.  Access the frontend at `http://localhost:3000`.
5.  View logs:
    ```bash
    docker-compose logs -f
    ```

---

## Option 2: Deploy Frontend to Vercel

Vercel provides excellent hosting for Vite-based React applications.

1.  Create a [Vercel account](https://vercel.com) and connect your GitHub repository.
2.  Create a New Project and select the `smart-expense-tracker` repository.
3.  Configure Build Settings:
    -   **Framework Preset**: Vite
    -   **Root Directory**: `frontend`
    -   **Build Command**: `npm run build`
    -   **Output Directory**: `dist`
4.  Set Environment Variables:
    -   `VITE_API_URL`: URL of your deployed backend (e.g., `https://my-backend.onrender.com`)
5.  Click **Deploy**.
6.  (Optional) Configure a custom domain in the project settings.

---

## Option 3: Deploy Backend to Render

Render is a PaaS that easily hosts Dockerized web services.

1.  Create a [Render account](https://render.com) and connect your GitHub repository.
2.  Click **New Web Service** and select your repository.
3.  Configure the service:
    -   **Name**: `smart-expense-backend`
    -   **Root Directory**: `backend`
    -   **Environment**: Docker
    -   **Region**: Choose closest to you
4.  **Crucial Step - Persistent Storage**:
    -   Scroll down to Advanced and click **Add Disk**.
    -   Name: `data-disk`
    -   Mount Path: `/app/data`
    -   Size: 1GB (sufficient for JSON data)
5.  Set Environment Variables (see reference below).
6.  Click **Create Web Service**. Render will build and deploy the Docker image.

---

## Environment Variables Reference

### Backend (`backend/.env`)
| Variable | Description | Default |
| --- | --- | --- |
| `BACKEND_ENV` | Environment (`development`, `production`) | `development` |
| `CORS_ORIGINS` | Comma-separated list of allowed origins | `http://localhost:3000` |
| `DATA_DIR` | Path to store `data.json` | `/app/data` |

### Frontend (`frontend/.env`)
| Variable | Description | Default |
| --- | --- | --- |
| `VITE_API_URL` | Base URL for the API | `http://localhost:8000` |

---

## Production Checklist

Before going live, ensure you have completed the following:

- [ ] Set `BACKEND_ENV=production` on your backend server.
- [ ] Configure `CORS_ORIGINS` on the backend to match your Vercel frontend URL.
- [ ] Verify rate limiting is appropriate for your traffic expectations.
- [ ] Verify persistent storage (disk mount) is correctly configured for the JSON data file so data isn't lost on container restart.
- [ ] Test the `/health` endpoint after deployment.
- [ ] Verify HTTPS is working on both frontend and backend.
- [ ] Check that security headers are applied correctly.

---

## Troubleshooting

-   **Data loss on restart (Docker/Render)**: You forgot to configure a volume mount for `/app/data`. The container filesystem is ephemeral.
-   **CORS Errors in browser**: Ensure `VITE_API_URL` points to the correct backend and the backend's `CORS_ORIGINS` includes the exact URL of your deployed frontend.
-   **API calls failing**: Check if the backend URL uses `https://` in production. Mixed content (HTTP on HTTPS site) will be blocked by browsers.
