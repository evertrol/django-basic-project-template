The settings are split into several modules:

- one base module which defines settings for the project itself.
- one local module which defines settings for the environment, and
  will likely be different for different servers.
- extra modules for additional settings not suitable for the base or
  local settings, e.g. for optional packages.

The __init__.py module ties the modules all together.

Ideally, the base.py, __init__.py and possible extra module files are
committed to the repository, as well as an local module template, with
values missing. Each environment then has its own, private copy of the
local module, with details filled in (keys, database login details,
etc).

See also the comments in local_template.py, and __init__.py to see how
it is tied together.
