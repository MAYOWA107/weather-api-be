# weather-api-be
A Django REST API that fetches real-time weather data from OpenWeather, with Redis caching to improve performance and reduce external API calls. Includes Swagger documentation for easy testing.

## 🚀 Features

- 🌍 Fetch real-time weather data by city  
- ⚡ Redis caching (reduces API calls & improves speed)  
- 🧠 Clean architecture (View + Service separation)  
- 📘 Swagger (OpenAPI) documentation with DRF Spectacular  
- 🔐 Environment-based API key management  

---

## 🧱 Tech Stack

- Django  
- Django REST Framework  
- Redis  
- drf-spectacular (Swagger/OpenAPI)  
- OpenWeather API  

---

## 📂 Project Structure

```
weather_api/
│
├── weather_app/
│   ├── views.py          # Handles HTTP requests
│   ├── service.py        # External API logic
│   ├── serializers.py    # Response structure
│
├── core/
│   ├── settings.py       # App configuration (Redis, API keys)
│   ├── urls.py           # Routes
│
└── manage.py
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```
git clone https://github.com/MAYOWA107/weather-api.git
cd weather-api
```

---

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
WEATHER_API_KEY=your_openweather_api_key
```

---

### 5. Run migrations

```
python manage.py migrate
```

---

### 6. Start Redis server

Make sure Redis is running locally:

```
redis-server
```

---

### 7. Run development server

```
python manage.py runserver
```

---

## 🌐 API Usage

### Get Weather by City

```
GET /api/weather/{city}/
```

#### Example:

```
/api/weather/lagos/
```

---

### 🧪 Sample Response

```
{
  "city": "Lagos",
  "temperature": 27.5,
  "description": "light rain",
  "humidity": 82
}
```

---

## ⚡ Caching Strategy

- Cache key format: `weather:{city}`
- Cache duration: **12 hours**
- Reduces repeated external API calls
- Improves response speed significantly

---

## 📘 API Documentation (Swagger)

Interactive API docs available at:

```
/api/docs/
```

---

## 🧠 Architecture Overview

```
Client Request
      ↓
   View Layer
      ↓
   Cache (Redis)
   ↓        ↓
 HIT      MISS
  ↓         ↓
Response   Service Layer → OpenWeather API
                ↓
           Save to Cache
                ↓
             Response
```

---

## ❗ Notes

- Ensure your OpenWeather API key is active before testing  
- Redis must be running locally for caching to work  
- API responses are normalized for cleaner output  

---



## 🤝 Contributing

Feel free to fork this project and submit pull requests.

---

