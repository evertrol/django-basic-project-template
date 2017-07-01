from .base import *
# Attempt to add local settings
try:
    from .local import *
except ImportError:
    pass

# Add any extra settings that should come after local
try:
    from .extra import *
except ImportError:
    pass
