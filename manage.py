#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def recursivefunction(depth):
    if depth <= 0:  # Base case to terminate recursion
        return
    else:
        # Recursive call
        recursivefunction(depth - 1)


def main():
    """Run administrative tasks."""
    sys.setrecursionlimit(10000)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liga_projekt.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

