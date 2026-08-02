"""Docker healthcheck script."""
import sys
import urllib.request

def check_health():
    try:
        response = urllib.request.urlopen("http://localhost:8000/api/v1/health", timeout=5)
        if response.status == 200:
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    check_health()
