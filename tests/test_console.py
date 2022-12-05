#!/usr/bin/python3
"""Test for console"""

import unittest
import pycodestyle
import sys
import tests
from io import StringIO
from unittest.mock import patch
import os
import json
import console
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """This class will test console"""

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_emptyline(self):
        """Test for empty line command"""
        with patch ('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('\n')
            self.assertEqual('',f.getvalue())

    # def test_quit(self):
    #     """Test for quit command"""
    #     with patch ('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd('quit')
    #         self.assertEqual('',f.getvalue())

    # def test_EOF(self):
    #     """Handles EOF to exit the program"""
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("EOF")
    #     msg = f.getvalue()
    #     self.assertTrue(len(msg) == 1)
    #     self.assertEqual("\n", msg)
    #     with patch('sys.stdout',new=StringIO()) as f:
    #         HBNBCommand().onecmd("EOF console")
    #         message = f.getvalue()
    #         self.assertTrue(len(message) == 1)
    #         self.assertEqual("\n",message)

    def test_create(self):
        """Test the create command in the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            message = ' **class name missing** '
            self.assertTrue(message,f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create asdfgh")
            message =' **class doesnt exist** '
            self.assertTrue(message,f.getvalue())   
        with patch(sys.stdout, new=StringIO()) as f:
            HBNBCommand().onecmd("create User email=test@test.com password=password")
        with patch(sys.stdout, new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertTrue("[User]".f.getvalue()[-1])    