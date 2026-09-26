from app.compat import Plugin, check_plugins


def test_loads_compatible_and_rejects_incompatible():
    report = check_plugins(
        "1.5.0",
        [
            Plugin(name="audit-log", version="0.3.0", requires_host=">=1.4, <2.0"),
            Plugin(name="legacy-sync", version="0.1.0", requires_host="<1.2"),
        ],
    )
    assert report.loadable == ["audit-log"]
    assert "legacy-sync" in report.rejected
