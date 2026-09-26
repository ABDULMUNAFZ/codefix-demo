from app.versions import satisfies


def test_satisfies_accepts_host_version_with_prerelease_suffix():
    assert satisfies("1.5.0-rc1", ">=1.4, <2.0") is True
