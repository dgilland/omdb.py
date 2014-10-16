## v0.1.1, 2014-02-09

- Python3 support ([agronholm](https://github.com/agronholm)).
- PEP8 compliance excluding max-line-length ([agronholm](https://github.com/agronholm)).
- Wheel support ([agronholm](https://github.com/agronholm)).

## v0.1.0, 2013-11-24

- Convert API response to data models (see omdb/models.py).
- Add /tests folder and move appropriate doctests there.
- Return empty data for `search` and `get` requests which return no record(s).
- Add `omdb.set_default()` for setting default request parameters (e.g. `set_default(tomatoes=True)` to always include tomatoes data)

## v0.0.1, 2013-11-12

- Initial release.
