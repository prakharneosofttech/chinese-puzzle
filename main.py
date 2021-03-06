from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/get_count")
def get_count(head_count:int, leg_count:int):
    """
    Endpoint where you can fill in the values for head_count & leg_count to formulate the common classic 
    ancient Chinese puzzle: We count head_count heads and leg_count legs among the chickens and rabbits 
    in a farm. How many rabbits and how many chickens do we have? then returns the answer as a JSON.
    """
    error_msg="No solution"
    if(head_count>=leg_count):
        raise HTTPException(status_code=400, detail= error_msg)
    elif(leg_count%2!=0):
        raise HTTPException(status_code=400, detail= error_msg)
    elif(leg_count/2 < head_count):
        raise HTTPException(status_code=400, detail= error_msg)
    else:
        rabbit_count=(leg_count-2*head_count)/2
        chicken_count=head_count-rabbit_count
    return {"rabbits": int(rabbit_count), "chickens": int(chicken_count), "success": True}
