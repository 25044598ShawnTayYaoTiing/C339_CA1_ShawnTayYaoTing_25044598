
import pytest
from library_fine import calculate_fine


# TEST 1: Verify fine calculation at 50 cents per overdue day.
# Uses boundary values to check that there is no maximum fine.
@pytest.mark.parametrize("days_overdue, expected", [
    (0, 0),       # No overdue days
    (1, 50),      # Minimum positive overdue days
    (5, 250),     # Normal overdue period
    (9, 450),     # Below the 10-day boundary
    (10, 500),    # At the 10-day boundary
    (11, 550),    # Detects incorrect 10-day cap
    (20, 1000),   # Verifies fine continues increasing
])
def test_fine_in_cents(days_overdue, expected):
    result = calculate_fine(days_overdue)

    assert result == expected
    assert type(result) is int


# TEST 2: Verify that negative overdue days raise ValueError.
def test_negative_days():
    with pytest.raises(ValueError):
        calculate_fine(-1)


# TEST 3: Verify that non-integer inputs raise TypeError.
@pytest.mark.parametrize("days_overdue", [1.5, "1", None, True])
def test_invalid_days_type(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
