from fastapi.responses import JSONResponse


def success(data=None, message="Success"):
    return JSONResponse(status_code=200, content={"data": data, 'message': message})

def error(data=None, message="Error", code=400):
    return JSONResponse(status_code=code, content={"errors": [{'message': message}]})

