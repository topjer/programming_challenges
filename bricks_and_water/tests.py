import pytest
from main import how_much_water

@pytest.mark.parametrize("input, expected_outcome", [([2,0,2], 2), ([3,1,0,3], 5)])
def test_borders_highest_and_same_heigt(input, expected_outcome):
    outcome = how_much_water(input)

    assert outcome == expected_outcome

@pytest.mark.parametrize("input, expected_outcome", [([1,0,2,1], 1), ([3,0,6,1,0,3], 8)])
def test_higher_blocks_inside(input, expected_outcome):
    outcome = how_much_water(input)

    assert outcome == expected_outcome

@pytest.mark.parametrize("input, expected_outcome", [([0,1,0,2,1], 1), ([0,0,3,0,6,1,0,3,0,0,0], 8)])
def test_zero_boundaries(input, expected_outcome):
    outcome = how_much_water(input)

    assert outcome == expected_outcome

@pytest.mark.parametrize("input, expected_outcome", [([5,0,3,0,1], 4)])
def test_descending_array(input, expected_outcome):
    outcome = how_much_water(input)

    assert outcome == expected_outcome