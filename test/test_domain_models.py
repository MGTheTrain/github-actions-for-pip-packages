from datetime import datetime
from domain.models.user import User
import pytest
from pydantic import ValidationError


@pytest.fixture
def valid_user():
    return User(
        userId="123",
        userName="ValidUserName123",
        userPassword="StrongPassword123!?§$%",
        email="test@example.com",
        dateTimeCreated=datetime.now(),
        dateTimeUpdated=datetime.now(),
    )


def test_user_validation(valid_user):
    # Test valid user data
    assert valid_user is not None

    # Testing valid user data
    try:
        valid_user_dict = valid_user.dict()
        User(**valid_user_dict)
    except ValidationError as e:
        pytest.fail(f"Validation raised unexpected ValidationError: {e}")


def test_user_password_complexity():
    # Invalid password complexity
    with pytest.raises(
        ValueError, match="userPassword does not meet complexity requirements."
    ):
        invalid_user = User(
            userId="123",
            userName="ValidUserName123",
            userPassword="weakpassword",
            email="test@example.com",
            dateTimeCreated=datetime.now(),
            dateTimeUpdated=datetime.now(),
        )
        invalid_user_dict = invalid_user.dict()
        User(**invalid_user_dict)
