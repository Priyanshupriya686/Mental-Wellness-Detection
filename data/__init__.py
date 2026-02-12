"""
Data loading utilities for Mental Wellness Detection.

This package provides robust functions to load and validate datasets
from the Datasets/ directory.
"""

from .loaders import (
    load_social_media_mental_health,
    load_train,
    load_val,
    load_test,
    load_all_splits,
    get_dataset_info,
    DataLoaderError
)

__all__ = [
    'load_social_media_mental_health',
    'load_train',
    'load_val',
    'load_test',
    'load_all_splits',
    'get_dataset_info',
    'DataLoaderError'
]