import pytest
import processor


def test_verify_csv_extension_valid():
    assert processor.verify_csv_extension("data/estudiantes.csv") is True


def test_verify_csv_extension_none():
    assert processor.verify_csv_extension(None) is False


def test_verify_csv_extension_empty():
    assert processor.verify_csv_extension("") is False


def test_verify_csv_extension_invalid():
    assert processor.verify_csv_extension("data/estudiantes.json") is False


def test_evaluate_age_valid():
    assert processor.evaluate_age(21) is True


def test_evaluate_age_zero():
    assert processor.evaluate_age(0) is False


def test_evaluate_age_negative():
    assert processor.evaluate_age(-5) is False


def test_evaluate_average_valid():
    assert processor.evaluate_average(8.5) is True


def test_evaluate_average_min_limit():
    assert processor.evaluate_average(0) is True


def test_evaluate_average_max_limit():
    assert processor.evaluate_average(10) is True


def test_evaluate_average_below_range():
    assert processor.evaluate_average(-1) is False


def test_evaluate_average_above_range():
    assert processor.evaluate_average(11) is False


def test_evaluate_name_valid():
    assert processor.evaluate_name("Ana") is True


def test_evaluate_name_empty():
    assert processor.evaluate_name("") is False


def test_evaluate_name_single_space():
    assert processor.evaluate_name(" ") is False

    
def test_verify_csv_extension_wrong_type():
    assert processor.verify_csv_extension(123) is False


def test_evaluate_age_none():
    assert processor.evaluate_age(None) is False


def test_evaluate_age_wrong_type():
    assert processor.evaluate_age("20") is False


def test_evaluate_average_none():
    assert processor.evaluate_average(None) is False


def test_evaluate_average_wrong_type():
    assert processor.evaluate_average("8.5") is False


def test_evaluate_name_none():
    assert processor.evaluate_name(None) is False