# Safe application
import os

# Safe: debug mode from environment
DEBUG = os.getenv("DEBUG", "False") == "True"

# Safe: no hardcoded secrets
DATABASE_URL = os.getenv("DATABASE_URL")

# Safe: parameterized query
def safe_query(user_id):
    return "SELECT * FROM users WHERE id = %s", (user_id,)

# Safe: no shell=True
def safe_run(cmd):
    import subprocess
    subprocess.call([cmd])