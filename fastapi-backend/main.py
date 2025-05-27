from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

# Create an instance of FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only; allow any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "T-Shirt",
        "price": 25,
        "image": "https://images.unsplash.com/photo-1581655353564-df123a1eb820?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "id": 2,
        "name": "Sneakers",
        "price": 80,
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c25lYWtlcnN8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 3,
        "name": "Backpack",
        "price": 45,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmFja3BhY2t8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 4,
        "name": "Watch",
        "price": 120,
        "image": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8d2F0Y2h8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 5, 
        "name": "Laptop Bag",
        "price": 65, 
        "image": "https://plus.unsplash.com/premium_photo-1680392544041-d89413b561ce?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bGFwdG9wJTIwYmFnfGVufDB8fDB8fHww"
    },
    {
        "id": 6, 
        "name": "Baseball Cap", 
        "price": 15, 
        "image": "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YmFzZWJhbGwlMjBjYXB8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 7,
        "name":"Wireless Earbuds",
        "price": 99,
        "image": "https://images.unsplash.com/photo-1627989580309-bfaf3e58af6f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8d2lyZWxlc3MlMjBlYXJidWRzfGVufDB8fDB8fHww"
    },
    {
        "id": 8,
        "name": "Jacket", 
        "price": 85, 
        "image": "https://images.unsplash.com/photo-1611312449408-fcece27cdbb7?q=80&w=1869&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "id": 9, 
        "name": "Sunglasses",
        "price": 55, 
        "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3VuZ2xhc3Nlc3xlbnwwfHwwfHx8MA%3D%3D"
    },
    {
        "id": 10,
        "name": "Yoga Mat", 
        "price": 30, 
        "image": "https://images.unsplash.com/photo-1591291621164-2c6367723315?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8eW9nYSUyMG1hdHxlbnwwfHwwfHx8MA%3D%3D"
    },
]

# Root endpoint (http://127.0.0.1:8000/)
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    # If product not found, raise 404 error
    raise HTTPException(status_code=404, detail="Product not found")