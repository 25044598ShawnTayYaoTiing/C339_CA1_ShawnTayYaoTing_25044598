
import pytest
from library_eligibility import can_borrow


# TEST 1: Verify borrowing eligibility based on active and overdue loans.
# Requirement: Fewer than 5 active loans and no overdue books.
@pytest.mark.parametrize("active_loans, overdue_books, expected", [
    (0, 0, True),    # No active or overdue loans
    (4, 0, True),    # Below the 5-loan boundary
    (5, 0, False),   # Detects incorrect 5-loan allowance
    (6, 0, False),   # Above the borrowing limit
    (0, 1, False),   # Overdue books prevent borrowing
    (5, 1, False),   # Both restrictions apply
])
def test_borrowing_eligibility(active_loans, overdue_books, expected):
    result = can_borrow(active_loans, overdue_books)

    assert result is expected


# TEST 2: Verify that negative loan counts raise ValueError.
@pytest.mark.parametrize("active_loans, overdue_books", [
    (-1, 0),  # Negative active loans
    (0, -1),  # Negative overdue books
])
def test_negative_borrowing_values(active_loans, overdue_books):
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)


# TEST 3: Verify that non-integer active loan counts raise TypeError.
@pytest.mark.parametrize("invalid_value", [1.5, "1", None, True])
def test_invalid_active_loans_type(invalid_value):
    with pytest.raises(TypeError):
        can_borrow(invalid_value, 0)


# TEST 4: Verify that non-integer overdue book counts raise TypeError.
@pytest.mark.parametrize("invalid_value", [1.5, "1", None, True])
def test_invalid_overdue_books_type(invalid_value):
    with pytest.raises(TypeError):
        can_borrow(0, invalid_value)
