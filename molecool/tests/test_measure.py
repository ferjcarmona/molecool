"""
Test for the measure module. 
"""

#imports

import pytest
import molecool
import numpy as np

def test_calculate_distance():

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1,r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():

    rA = np.array([0,0,-1])
    rB = np.array([0,0,0])
    rC = np.array([1,0,0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(rA,rB,rC, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle

@pytest.mark.parametrize("p1,p2,p3, expected_angle", [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60  ),
    (np.array([np.sqrt(3)/2, (1/2), 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 30),
])
def test_calculate_angle_many(p1,p2,p3, expected_angle):

    calculated_value = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_value