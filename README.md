h1 style="color:#2c3e50;">🚀 FastAPI Auth App</h1>

<p style="font-size:16px;">
A lightweight FastAPI project with <strong>JWT-based authentication</strong> and <strong>MongoDB Cloud</strong>.
</p>

<h2 style="color:#007acc;">📌 Features</h2>
<ul>
  <li><span style="color:green;">JWT login/register</span></li>
  <li><span style="color:green;">Protected user routes</span></li>
  <li><span style="color:green;">MongoDB Cloud integration</span></li>
  <li><span style="color:green;">CRUD operations</span></li>
  <li><span style="color:green;">Password hashing with <code>passlib</code></span></li>
</ul>

<h2 style="color:#007acc;">🚀 Getting Started</h2>
<p>To run the project locally:</p>

<pre>
<code>pip install -r requirements.txt
uvicorn app.main:app --reload</code>
</pre>

<h2 style="color:#007acc;">📁 Project Structure</h2>
<ul>
  <li><code>app/main.py</code> – FastAPI app instance and routes</li>
  <li><code>app/api/routes_auth.py</code> – user registration and login operations</li>
  <li><code>app/db/models.py</code> – Pydantic models</li>
  <li><code>app/core/auth.py</code> – JWT utilities and authentication logic</li>
  <li><code>app/core/config.py</code> – project name and secret keys</li>
  <li><code>app/db/database.py</code> – MongoDB Cloud connection</li>
  <li><code>app/api/routes_user.py</code> – token login and CRUD operations on users</li>
  <li><code>app/schemas/schemas.py</code> – login token models</li>
</ul>

<h2 style="color:#007acc;">🔐 Authentication</h2>
<p>
Users receive a JWT token upon login. Send it in the <code>Authorization</code> header as a Bearer token for protected routes.
</p>

<h2 style="color:#007acc;">🌐 MongoDB Cloud</h2>
<p>
Set up a MongoDB Atlas cluster and add your connection string in <code>app/database.py</code>.
</p>

<h2 style="color:#007acc;">✅ Example <code>.env</code> File</h2>
<pre><code>MONGO_URL="your_mongodb_connection_string"
JWT_SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30</code></pre>

<h2 style="color:#007acc;">🛠️ Requirements</h2>
<pre><code>fastapi
uvicorn
pymongo
python-jose
passlib[bcrypt]
python-dotenv</code></pre>
