import pytest
from main import calculate_roi

def test_positive_roi():
    """Тест стандартного прибуткового сценарію"""
    assert calculate_roi(100, 150) == 50.0

def test_negative_roi():
    """Тест збиткового сценарію"""
    assert calculate_roi(100, 50) == -50.0

def test_zero_profit():
    """Тест виходу в нуль"""
    assert calculate_roi(100, 100) == 0.0

def test_invalid_investment():
    """Тест обробки некоректних даних (нульова інвестиція)"""
    with pytest.raises(ValueError):
        calculate_roi(0, 100)

def test_negative_investment():
    """Тест обробки від'ємної інвестиції"""
    with pytest.raises(ValueError):
        calculate_roi(-50, 100)