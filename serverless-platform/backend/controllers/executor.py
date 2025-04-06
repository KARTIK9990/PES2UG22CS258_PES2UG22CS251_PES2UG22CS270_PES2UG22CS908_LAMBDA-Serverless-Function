import subprocess
import uuid
import os

def run_function(language: str, code: str, timeout: int):
    file_id = str(uuid.uuid4())
    filename = f"/tmp/{file_id}.{'py' if language == 'python' else 'js'}"
    image = "python-runner" if language == "python" else "js-runner"

    with open(filename, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["docker", "run", "--rm", "-v", f"{filename}:/app/code.{language[:2]}", image],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout
        )
        output = result.stdout.decode()
        error = result.stderr.decode()
        return {"output": output, "error": error}
    except subprocess.TimeoutExpired:
        return {"error": "Function execution timed out."}
    finally:
        os.remove(filename)
