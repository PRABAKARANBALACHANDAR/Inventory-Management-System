from fastapi import FastAPI,Request,status
from fastapi.responses import JSONResponse

class AppException(Exception):
    def __init__(self,detail:str,status_code:int=status.HTTP_400_BAD_REQUEST):
        self.detail=detail
        self.status_code=status_code

class NotFoundException(AppException):
    def __init__(self,detail:str="Resource not found"):
        super().__init__(detail,status.HTTP_404_NOT_FOUND)

class ConflictException(AppException):
    def __init__(self,detail:str="Resource already exists"):
        super().__init__(detail,status.HTTP_409_CONFLICT)

class UnauthorizedException(AppException):
    def __init__(self,detail:str="Unauthorized",status_code:int=status.HTTP_401_UNAUTHORIZED):
        super().__init__(detail,status_code)

class BadRequestException(AppException):
    def __init__(self,detail:str="Bad request"):
        super().__init__(detail,status.HTTP_400_BAD_REQUEST)

async def app_exception_handler(request:Request,exc:AppException):
    return JSONResponse(status_code=exc.status_code,content={"detail":exc.detail})

def register_exception_handlers(app:FastAPI):
    app.add_exception_handler(AppException,app_exception_handler)
