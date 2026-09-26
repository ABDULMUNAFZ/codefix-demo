"""Usage: python -m app.cli HOST_VERSION PLUGINS_JSON"""

from __future__ import annotations

import json
import sys

from app.compat import Plugin, check_plugins


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    host_version, path = argv
    with open(path, encoding="utf-8") as handle:
        plugins = [Plugin(**item) for item in json.load(handle)]
    report = check_plugins(host_version, plugins)
    print(json.dumps({"loadable": report.loadable, "rejected": report.rejected}, indent=2))
    return 0 if not report.rejected else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
