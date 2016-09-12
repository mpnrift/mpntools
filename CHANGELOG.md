# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 0.2.0 - 2016-09-12

### Added
- Function get_substr_all().
- Tests for get_substr_all().

### Changed
- Refactored get_substr() and get_nested_val() for cleaner code.
- Modified get_substr() docstring.
- Both get_substr() and get_nested_val() now return ValueError if parameters are invalid.
- Modified tests to use raised ValueError exceptions.


## 0.1.1 - 2016-08-30

### Added
- Added pytest requirement in setup.py.

### Changed
- Refactored and cleaned up get_substr().
- Refactored and cleaned up get_nested_val().
- Updated README.md.


## 0.1.0 - 2016-08-30

### Added
- Function get_substr().
- Function get_nested_val().
- Pytest tests for currently implemented functions
- Properly formatted CHANGELOG.md