from maths import add
import pytest
# Happy path!

def test_two_whole_numbers_add_together_correctly():
  # Arrange  - Given
  number1 = 10
  number2 = 20
  expected = 30

  # Act      - When
  result = add(number1, number2)

  # Assert   - Then
  assert result == expected


def test_two_decimals_add_correctly():
  assert add(0.1, 0.2) == pytest.approx(0.3, 8)

# Parameterize my test
# Decorate my function
@pytest.mark.parametrize(
  "num1, num2, expected",
  [
    (-100, -100, -200),
    (1_000_000, 1_000_000, 2_000_000),
    (3_000_000, 10, 3_000_010),
    (-100, 100, 0)
  ]
)
def test_adding_various_numbers(num1, num2, expected):
  assert add(num1, num2) == expected

# Test Driven Development - TDD
# Unit -> Integration/Service -> E2E

def test_it_fails_when_adding_strings():
  with pytest.raises(TypeError):
    add("1", "2")

@pytest.mark.parametrize(
  "num1, num2",
  [
    ([], []),
    (1, []),
    ({}, 5),
    (True, 6)
  ]
)
def test_adding_various_non_numbers(num1, num2):
  with pytest.raises(TypeError):
    add(num1, num2)