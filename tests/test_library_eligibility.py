import pytest

from library_eligibility import can_borrow


@pytest.mark.parametrize("active_loans, overdue_books, expected", [
    (0, 0, True),
    (4, 0, True),
    (5, 0, False),
    (6, 0, False),
    (0, 1, False),
    (5, 1, False),
])
def test_borrowing_eligibility(active_loans, overdue_books, expected):
    result = can_borrow(active_loans, overdue_books)

    assert result is expected


@pytest.mark.parametrize("active_loans, overdue_books", [
    (-1, 0),
    (0, -1),
])
def test_negative_borrowing_values(active_loans, overdue_books):
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)


@pytest.mark.parametrize("invalid_value", [1.5, "1", None, True])
def test_invalid_active_loans_type(invalid_value):
    with pytest.raises(TypeError):
        can_borrow(invalid_value, 0)


@pytest.mark.parametrize("invalid_value", [1.5, "1", None, True])
def test_invalid_overdue_books_type(invalid_value):
    with pytest.raises(TypeError):
        can_borrow(0, invalid_value)
