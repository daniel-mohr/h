"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-05-17
:License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.

tests the script 'pfu.py speed_test'

You can run this file directly::

  env python3 script_pfu_speed_test.py

  pytest-3 script_pfu_speed_test.py

Or you can run only one test, e. g.::

  env python3 script_pfu_speed_test.py script_pfu_speed_test.test_script_pfu_speed_test_1

  pytest-3 -k test_script_pfu_speed_test_1 script_pfu_speed_test.py
"""

import os
import re
import subprocess
import tempfile
import unittest


class script_pfu_speed_test(unittest.TestCase):
    """
    :Author: Daniel Mohr
    :Date: 2021-05-17
    """

    def test_script_pfu_speed_test_1(self):
        """
        :Author: Daniel Mohr
        :Date: 2021-05-17
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            param = '-f a -bytes 42 -count 6 '
            cp = subprocess.run(
                ['pfu.py speed_test ' + param],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                shell=True,
                timeout=3, check=True)
            self.assertTrue(cp.stderr.endswith(b'finished.\n'))


if __name__ == '__main__':
    unittest.main(verbosity=2)