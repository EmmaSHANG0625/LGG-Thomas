from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#define the model
class SalaryRequest(BaseModel):
    salary: Optional[float] = None
    bonus: Optional[float] = None
    taxes: Optional[float] = None

@app.get("/")
async def read_root():
    return {"message": "welcome!"}

@app.post("/multiply")
async def multiply_number(number: float):
    return {"result": number * 2}

@app.post("/caculate")
async def caculate_salary(request: SalaryRequest):
    #check for missing fields
    missing_fields = []
    if request.salary is None:
        missing_fields.append('salary')
    if request.bonus is None:
        missing_fields.append('bonus')
    if request.taxes is None:
        missing_fields.append('taxes')
    
    if missing_fields:
        missing_fields_str = ", ".j
        raise HTTPException(status_code=400, detail=f"3 fields expected (salary, bonus, taxes). You forgot: {missing_fields_str}.")
    # Validate types and perform computation
    try:
        salary = float(request.salary)
        bonus = float(request.bonus)
        taxes = float(request.taxes)
    except ValueError:
        raise HTTPException(status_code=400, detail="expected numbers, got strings.")
    
    result = salary + bonus - taxes
    return {"result": result}