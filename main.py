import time
from functools import wraps
from fastapi import FastAPI, Request, HTTPException, status
from collections import defaultdict

app = FastAPI()

# Rate limiting storage
rate_limit_storage = defaultdict(lambda: {"count": 0, "time": time.time()})

# Configurations
API_KEY = "secret-api-key"
RATE_LIMIT = 5  # requests per minute

def measure_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        response = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time:.4f} seconds")
        return response
    return wrapper

def log_request(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        method = request.method
        url = request.url.path
        print(f"Request: {method} {url}")
        return await func(request, *args, **kwargs)
    return wrapper

def api_key_required(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key != API_KEY:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key")
        return await func(request, *args, **kwargs)
    return wrapper

def rate_limiter(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        client_ip = request.client.host
        current_time = time.time()
        data = rate_limit_storage[client_ip]
        if current_time - data["time"] > 60:
            data["count"] = 0
            data["time"] = current_time
        data["count"] += 1
        if data["count"] > RATE_LIMIT:
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded")
        return await func(request, *args, **kwargs)
    return wrapper

@app.get("/")
@measure_time
@log_request
@api_key_required
@rate_limiter
async def read_root(request: Request):
    return {"message": "Hi Muzamil, you are seeing this message because you have a valid key. Congrats !!"}

@app.get("/items/{item_id}")
@measure_time
@log_request
@api_key_required
@rate_limiter
async def read_item(request: Request, item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
