import pytest

from app.versions import InvalidVersion, compare, parse_version, satisfies


def test_parse_version_accepts_v_prefix():
    assert parse_version("v1.2.3") == parse_version("1.2.3")


def test_parse_version_rejects_garbage():
    with pytest.raises(InvalidVersion):
        parse_version("1.x")


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("1.2.3", "1.2.3", 0),
        ("1.2", "1.2.0", 0),
        ("1.2.4", "1.2.3", 1),
        ("1.3.0", "1.2.9", 1),
        ("2.0.0", "1.9.9", 1),
        ("0.9.0", "1.0.0", -1),
    ],
)
def test_compare(a, b, expected):
    assert compare(a, b) == expected


@pytest.mark.parametrize(
    ("version", "requirement", "expected"),
    [
        ("1.4.0", ">=1.4", True),
        ("1.3.9", ">=1.4", False),
        ("1.5.2", ">=1.4, <2.0", True),
        ("2.0.0", ">=1.4, <2.0", False),
        ("1.4.0", "==1.4.0", True),
        ("1.4.1", "!=1.4.0", True),
    ],
)
def test_satisfies(version, requirement, expected):
    assert satisfies(version, requirement) is expected


def test_satisfies_rejects_bad_clause():
    with pytest.raises(ValueError):
        satisfies("1.0.0", "~1.0")
