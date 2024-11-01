from fastapi import status, HTTPException


resource_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Requested Resource Not Found."
)

unauthorized_access = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect Email Or Password.",
    headers={"WWW-Authenticate": "Bearer"},
)

credentials_validation_failure = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could Not Validate Credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

duplicate_email = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Email Address Already In Use"
)
