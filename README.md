# codefix-demo

Small plugin-compatibility checker used as the target repository for the
[CodeFix](https://github.com/ABDULMUNAFZ/codefix-agent) agent demo.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest
python -m app.cli 1.5.0 plugins.json
```

`app/versions.py` parses versions and evaluates requirement clauses such as
`>=1.4, <2.0`; `app/compat.py` decides which plugins can load on a host version.
