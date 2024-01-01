from web.dtos.user_request_dto import UserRequestDto
from pydantic import ValidationError
import pytest


@pytest.fixture
def valid_user_request():
    return UserRequestDto(
        userName="ValidUserName123",
        userPassword="StrongPassword123!?§$%",
        email="test@example.com",
    )


def test_user_request_validation(valid_user_request):
    # Test valid user request data
    assert valid_user_request is not None

    # Testing valid user request data
    try:
        valid_user_request_dict = valid_user_request.dict()
        UserRequestDto(**valid_user_request_dict)
    except ValidationError as e:
        pytest.fail(f"Validation raised unexpected ValidationError: {e}")


def test_user_request_password_complexity():
    # Invalid password complexity
    with pytest.raises(
        ValueError, match="userPassword does not meet complexity requirements."
    ):
        invalid_user_request = UserRequestDto(
            userName="ValidUserName123",
            userPassword="weakpassword",
            email="test@example.com",
        )
        invalid_user_request_dict = invalid_user_request.dict()
        UserRequestDto(**invalid_user_request_dict)
