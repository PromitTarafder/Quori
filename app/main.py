from fastapi import FastAPI

app = FastAPI(
    title= "Quori",
    description= "An API to track expenses and anlyzing spending patterns.",
    version= "0.1.0"
)

@app.get("/")
def hello():
    return {"message" : "This is Cowrie."}

@app.get("/health")
def health_check():
    return {"status" : "Healthy"}

