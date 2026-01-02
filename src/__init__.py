"""Pure Python Snappy compression library.

Snappy is a fast compression/decompression algorithm developed by Google.
It prioritizes speed over compression ratio, making it ideal for real-time
applications and network protocols.

Usage:

    from src import compress, decompress

    # Compress data before sending
    compressed = compress(data)

    # Decompress received data
    original = decompress(compressed)

The implementation follows the Snappy format specification:
https://github.com/google/snappy/blob/main/format_description.txt

Features:
- Pure Python implementation (no external dependencies)
- Full compatibility with Google's Snappy format
- Streaming-friendly block-based compression
- Comprehensive error handling with clear messages

Architecture:
- constants.py: Algorithm parameters and wire format constants
- encoding.py: Low-level varint and tag byte encoding/decoding
- compress.py: Compression algorithm (finding matches, emitting tags)
- decompress.py: Decompression algorithm (parsing tags, copying data)
"""

from __future__ import annotations

from .compress import compress, max_compressed_length
from .decompress import (
    SnappyDecompressionError,
    decompress,
    get_uncompressed_length,
    is_valid_compressed_data,
)

__all__ = [
    # Core API
    "compress",
    "decompress",
    # Utilities
    "max_compressed_length",
    "get_uncompressed_length",
    "is_valid_compressed_data",
    # Exceptions
    "SnappyDecompressionError",
]
