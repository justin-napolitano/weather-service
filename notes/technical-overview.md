---
slug: github-weather-service-note-technical-overview
id: github-weather-service-note-technical-overview
title: Weather Service Overview
repo: justin-napolitano/weather-service
githubUrl: https://github.com/justin-napolitano/weather-service
generatedAt: '2025-11-24T18:49:27.249Z'
source: github-auto
summary: >-
  The `weather-service` is a lightweight weather API built with FastAPI. It
  provides a few straightforward endpoints for accessing weather data.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

The `weather-service` is a lightweight weather API built with FastAPI. It provides a few straightforward endpoints for accessing weather data.

### Key Features:
- **GET /run?city={city}**: Fetches one-line weather info for the specified city in JSON format.
- **GET /push**: Sends the morning weather update to a specified notifier-gateway.
- **GET /healthz**: A simple health check to verify that the service is running.

### Quick Start:
1. Clone the repo:
   ```bash
   git clone https://github.com/justin-napolitano/weather-service.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather-service
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Gotchas:
Make sure your notifier-gateway is properly configured to receive the `/push` updates. Otherwise, you won't get those morning notifications.
