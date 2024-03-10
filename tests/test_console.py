#!/usr/bin/python3
"""Test console.py."""

import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage


class TestHBNBCommand_prompt(unittest.TestCase):
    """Tests for prompt."""

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Test help command."""

    def test_help_quit(self):
        h = "Exit the program."
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(h, f.getvalue().strip())

    def test_help_create(self):
        h = (
            "Usage: create <class>\n        "
            "Creates a new class instance and prints its id."
        )
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(h, f.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(h, f.getvalue().strip())

    def test_help_show(self):
        h = (
            "Usage: show <class> <id> or <class name>.show(<id>)\n        "
            "Display the string representation of a name or id."
        )
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(h, f.getvalue().strip())

    def test_help_destroy(self):
        h = (
            "Usage: destroy <class> <id> or <class name>.destroy(<id>)\n"
            "        Delete a class instance given an id."
        )
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(h, f.getvalue().strip())

    def test_help_all(self):
        h = (
            "all or all class or <class>.all().\n        "
            "Display string representation of all instances "
            "based or not on class."
        )
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(h, f.getvalue().strip())

    def test_help_count(self):
        h = (
            "Usage: count <class> or <class>.count()\n        "
            "Retrieve the number of instances of a class."
        )
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(h, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
