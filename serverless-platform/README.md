<h1>🚀 Serverless Function Execution Platform</h1>

<p>This project is a serverless execution platform similar to AWS Lambda. It allows users to upload and execute Python and JavaScript functions securely using Docker containers.</p>

<h2>📁 Project Structure</h2>
<pre>
serverless-platform/
├── backend/
├── docker/
│   ├── python/
│   └── javascript/
├── frontend/
├── uploaded_functions/
├── README.md
</pre>

<h2>⚙️ Local Setup Instructions</h2>

<h3>🔧 1. Clone the repository</h3>
<pre><code>git clone &lt;repo-url&gt;
</code></pre>

<h3>🐍 2. Setup Python Virtual Environment</h3>
<pre><code>sudo apt install python3-venv  # if venv not installed
python3 -m venv venv
source venv/bin/activate
</code></pre>

<h3>📦 3. Install Python Dependencies</h3>
<pre><code>pip install fastapi uvicorn pymongo python-multipart
cd serverless-platform</code></pre>

<h3>🐳 4. Build Docker Images</h3>
<pre><code># Build Python Docker runner
cd docker/python
docker build -t python-runner .

# Build JavaScript Docker runner
cd ../javascript
docker build -t js-runner .
</code></pre>

<h3>🍃 5. Start MongoDB (should be running locally)</h3>
<pre><code>sudo systemctl start mongod
</code></pre>

<h3>▶️ 6. Start the FastAPI Backend</h3>
<pre><code>cd ../..
uvicorn backend/main:app --reload
</code></pre>

<pre><p>open a new terminal and change directory to serverless-platform</p></pre>

<h2>🧪 API Testing with curl</h2>

<h3>📤 Upload a Python File</h3>
<pre><code>curl -X POST http://127.0.0.1:8000/functions/upload \
  -F "file=@uploaded_functions/hello.py" \
  -F "runtime=python"
</code></pre>

<h3>📤 Upload a JavaScript File</h3>
<pre><code>curl -X POST http://127.0.0.1:8000/functions/upload \
  -F "file=@uploaded_functions/hello.js" \
  -F "runtime=javascript"
</code></pre>

<h3>⚡ Execute a Function</h3>
<pre><code>curl -X POST http://127.0.0.1:8000/functions/&lt;function_id&gt;/execute
</code></pre>

<h3>📋 List All Functions</h3>
<pre><code>curl http://127.0.0.1:8000/functions/
</code></pre>

<h3>🗑️ Delete a Function</h3>
<pre><code>curl -X DELETE http://127.0.0.1:8000/functions/&lt;function_id&gt;
</code></pre>

<h2>🐳 Dockerfile Notes</h2>

<h4>🧪 Python Dockerfile (<code>docker/python/Dockerfile</code>)</h4>
<pre><code>FROM python:3.10-slim
WORKDIR /app
CMD ["python", "/code.py"]
</code></pre>

<h4>🧪 JavaScript Dockerfile (<code>docker/javascript/Dockerfile</code>)</h4>
<pre><code>FROM node:18-slim
WORKDIR /app
CMD ["node", "/code.js"]
</code></pre>

<h2>💡 Notes</h2>
<ul>
  <li>Make sure MongoDB is running locally and accessible on default port 27017</li>
  <li>Use proper file extensions (.py / .js) for uploaded code</li>
  <li>Execution uses Docker, so ensure you have <code>docker</code> installed and running</li>
</ul>

<h2>👥 Authors</h2>
<ul>
  <li>Developers: PES2UG22CS258, PES2UG22CS251, PES2UG22CS275, PES2UG22CS908</li>
</ul>
