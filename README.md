<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FastAPI Auth App</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 2rem; background: #f9f9f9; }
        h1, h2 { color: #333; }
        pre { background: #eee; padding: 1rem; border-radius: 5px; overflow-x: auto; }
        code { font-family: monospace; color: #c7254e; background-color: #f9f2f4; padding: 2px 4px; border-radius: 4px; }
        ul { margin-left: 1.5rem; }
    </style>
</head>
<body>
    <h1> FastAPI Auth App< /h1>
    <p>A lightweight FastAPI project with JWT-based authentication and MongoDB Cloud.</p>
    <h2>📌 Features</h2>
    <ul>
        <li>JWT login/register</li>
        <li>Protected user routes</li>
        <li>MongoDB Cloud integration</li>
        <li>CRUD operations on user data</li>
        <li>Password hashing with <code>passlib</code></li>
        <li>Scalable and secure backend architecture</li>
    </ul>
    <h2>🚀 Getting Started</h2>
    <p>To run the project locally, follow these steps:</p>
    <pre><code>pip install -r requirements.txt
uvicorn app.main:app --reload</code></pre>
    <h2>📁 Project Structure</h2>
    <ul>
        <li><code>app/main.py</code> - FastAPI app instance and routes</li>
        <li><code>app/models.py</code> - Pydantic models</li>
        <li><code>app/auth.py</code> - JWT utilities and authentication logic</li>
        <li><code>app/database.py</code> - MongoDB Cloud connection</li>
        <li><code>app/crud.py</code> - CRUD operations on users</li>
    </ul>
    <h2>🔐 Authentication</h2>
    <p>
        Users can register and log in to receive a JWT token. This token must be sent in the
        <code>Authorization</code> header as a Bearer token to access protected routes.
    </p>
    <h2>🌐 MongoDB Cloud</h2>
    <p>
        Ensure you have a MongoDB Atlas cluster running and update the connection string in
        <code>app/database.py</code> with your credentials.
    </p>
    <h2>✅ Example .env File</h2>
    <pre><code>MONGO_URL="your_mongodb_connection_string"
    JWT_SECRET_KEY="your_secret_key"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30</code></pre>
    <h2>🛠️ Requirements</h2>
    <pre><code>fastapi
    uvicorn
    pymongo cloud
    python-jose
    passlib[bcrypt]
    python-dotenv</code></pre>

</body>
</html>
