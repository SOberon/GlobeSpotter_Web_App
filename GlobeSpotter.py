import unittest
import pydoc
# from unittest.mock import patch # Remove; patch is usually for API calls


class main:

    def main(self):
        pass

    def parse_txt_file(input_file):
        """Parse a .txt file for IPv4 and IPv6 addresses.

        Args:
            input_file: A .txt file to be parsed.

        :return: A list of IP addresses.
        """
        import re

        file = open("temp.log")
        ipList = []

        for line in file:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
            ipList.append(ip)


class UnitTests(unittest.TestCase):

    def empty_test(self):
        pass

    if __name__ == "__main__": main()
