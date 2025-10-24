from fastapi import FastAPI
from starlette.middleware.method_override import MethodOverrideMiddleware


app = FastAPI()


# VULNERABLE: enable method override middleware
app.add_middleware(MethodOverrideMiddleware)


@app.delete("/api/secret")
async def secret():
# intentionally return the flag for the challenge
    try:
        with open('/flag.txt', 'r') as f:
            flag = f.read().strip()
    except Exception:
        flag = "FLAG_MISSING"
    return {"flag": flag}


@app.post("/api/public")
async def public():
    return {"msg": "public endpoint"}


@app.get("/")
async def index():
    return {"msg": "ok"}