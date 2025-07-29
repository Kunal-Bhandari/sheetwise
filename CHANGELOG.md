# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-07-30

### Added
- **Auto-Configuration**: New `auto_configure()` method that automatically optimizes compression settings based on spreadsheet characteristics (sparsity, size, data types)
- **Auto-Compress**: New `compress_with_auto_config()` method for one-step automatic optimization and compression
- **Multi-LLM Support**: Provider-specific output formats for ChatGPT, Claude, and Gemini via `encode_for_llm_provider()`
- **Enhanced CLI**: Support for `--auto-config`, `--format json`, `--verbose` flags with demo mode
- **Advanced Logging**: Optional detailed logging for debugging and monitoring compression operations
- **Enhanced Range Detection**: Improved `_merge_address_ranges()` method that creates ranges like `A1:A5` for contiguous cells
- **Contiguous Cell Grouping**: Enhanced `_group_contiguous_cells()` method for better data format aggregation
- **Comprehensive Test Suite**: Added `test_enhanced_features.py` with 6 new test cases
- **CSV Testing Tools**: Added demo scripts and test files for easy CSV testing
- **Format Comparison Tools**: Added utilities to compare different LLM output formats

### Enhanced
- **CLI Interface**: Can now combine `--demo` with `--vanilla`, `--auto-config`, `--format`, and `--stats` options
- **JSON Output**: Proper JSON serialization with numpy type handling
- **Error Handling**: Better error messages and validation
- **Code Coverage**: Increased test coverage to 34 passing tests

### Fixed
- **Range Detection**: Fixed incomplete implementation in address range merging
- **Cell Grouping**: Fixed placeholder implementation in contiguous cell detection
- **JSON Serialization**: Fixed numpy data type serialization issues
- **CLI Argument Handling**: Fixed argument parsing for combined flags

### Performance
- **Token Reduction**: Improved compression ratios, especially for sparse data (up to 5.5x reduction vs vanilla)
- **Format Optimization**: Provider-specific formats reduce token usage by 34-90% compared to general format
- **Auto-tuning**: Automatic parameter optimization based on data characteristics

### Documentation
- **README Updates**: Added documentation for all new features and CLI options
- **Format Guide**: Created comprehensive LLM format comparison documentation
- **Testing Guide**: Added CSV testing documentation and examples
- **API Reference**: Updated with new methods and parameters

## [1.0.0] - 2024-XX-XX

### Added
- Initial release of SheetWise
- Core compression framework with three modules
- Vanilla encoding methods
- Chain of Spreadsheet reasoning
- Basic CLI interface
- Comprehensive test suite
