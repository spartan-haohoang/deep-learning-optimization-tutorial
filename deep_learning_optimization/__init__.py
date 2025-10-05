"""
Deep Learning Optimization Tutorial Package

This package contains utilities and functions for deep learning model
optimization and tuning tutorials.
"""

__version__ = "0.1.0"
__author__ = "Learning Repository"
__email__ = "learning@example.com"

# Import common functions if they exist
try:
    from .common_functions import *  # noqa: F403, F401
except ImportError:
    pass

# Import model functions if they exist
try:
    from .model_functions import *  # noqa: F403, F401
except ImportError:
    pass
