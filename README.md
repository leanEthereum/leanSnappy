# leanSnappy

Pure Python implementation of Google's Snappy compression algorithm.

## Installation

```bash
uv sync
```

## Usage

```python
from src import compress, decompress

# Compress data
data = b"Hello, World!" * 100
compressed = compress(data)

# Decompress data
original = decompress(compressed)
assert original == data
```

## API

### Core Functions

- `compress(data: bytes) -> bytes`: Compress data using Snappy
- `decompress(data: bytes) -> bytes`: Decompress Snappy-compressed data

### Utilities

- `max_compressed_length(size: int) -> int`: Maximum possible compressed size
- `get_uncompressed_length(data: bytes) -> int`: Read uncompressed length from header
- `is_valid_compressed_data(data: bytes) -> bool`: Quick validation check

### Exceptions

- `SnappyDecompressionError`: Raised when decompression fails

## Development

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run linter
uv run ruff check src/ tests/

# Format code
uv run ruff format src/ tests/
```

## References

- [Google Snappy](https://github.com/google/snappy)
- [Format Description](https://github.com/google/snappy/blob/main/format_description.txt)

## License

MIT License
