Overview of the Project
This project is a FastAPI-based application that demonstrates the use of decorators to add various functionalities to API endpoints. The main functionalities added through decorators include measuring execution time, logging requests, API key-based authentication, and rate limiting. Below is an overview of what each part of the project does:

1. Main Functionalities
    Measure Execution Time:
    
    Decorator: measure_time
    Purpose: Measures the execution time of each API endpoint and prints it to the console. This is useful for performance monitoring and optimization.
    Log Requests:
    
    Decorator: log_request
    Purpose: Logs the HTTP method and URL of incoming requests. This helps in monitoring and debugging by keeping track of the API usage.
    API Key-Based Authentication:
    
    Decorator: api_key_required
    Purpose: Ensures that the requests to the API endpoints include a valid API key. This adds a layer of security to the API by allowing only        
    authenticated requests.
    Rate Limiting:
    
    Decorator: rate_limiter
    Purpose: Limits the number of requests that can be made from a single IP address within a certain time frame (e.g., 5 requests per minute). This 
    helps in preventing abuse and ensuring fair usage of the API.
2. API Endpoints
    Root Endpoint (/):
    
    Route: @app.get("/")
    Decorators: @measure_time, @log_request, @api_key_required, @rate_limiter
    Function: read_root
    Response: Returns a simple message {"message": "Hello, World!"}.
    Item Endpoint (/items/{item_id}):
    
    Route: @app.get("/items/{item_id}")
    Decorators: @measure_time, @log_request, @api_key_required, @rate_limiter
    Function: read_item
    Response: Returns the item ID and a name based on the ID, e.g., {"item_id": 1, "name": "Item 1"}.
3. Code Breakdown
    Rate Limiting Storage:
    
    Uses defaultdict to store request counts and timestamps for each IP address.
    Configurations:
    
    API_KEY: The secret key required for accessing the API.
    RATE_LIMIT: The maximum number of requests allowed per minute from a single IP address.
    Custom Decorators:
    
    measure_time: Wraps the endpoint function to measure and print its execution time.
    log_request: Wraps the endpoint function to log the request method and URL.
    api_key_required: Wraps the endpoint function to check for a valid API key in the request headers.
rate_limiter: Wraps the endpoint function to limit the number of requests based on the client's IP address.

4. Testing the Application
   Using Postman:
    Set up a GET request to http://127.0.0.1:8000/ with the header x-api-key: secret-api-key.
    Set up a GET request to http://127.0.0.1:8000/items/1 with the same header.

5.Conclusion
    This project demonstrates how to enhance a FastAPI application with additional functionalities using decorators. It provides a clean and modular        way to add logging, authentication, rate limiting, and performance monitoring to API endpoints. This approach helps in maintaining a clean codebase     by separating cross-cutting concerns from the core business logic.
