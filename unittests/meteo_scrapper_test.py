# -*- coding: utf-8 -*-
# !/usr/bin/env python

# MIT License
#
# Copyright (c) 2017 Maxime Busy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import unittest

from ariia import meteo_scrapper

class MeteoScrapperTest(unittest.TestCase):
	"""
	Unitest for the Meteo Scrapper
	"""


	def setUp(self):
		"""
		Setup for the test
		"""

        pass


	def test_constructor(self):
		"""
		Test the creation of the object
		"""

		logging.info("Create the object")
		scrapper = meteo_scrapper.MeteoScrapper()
		logging.info("Object correctly created")

		logging.info("Test object type")
		self.assertIsInstance(scrapper, meteo_scrapper.MeteoScrapper)
		logging.info("Object type correct")

	def test_getMeteo(self):
		"""
		Test method to get the meteo
		"""

		logging.info("Get the meteo, instanciate new meteo scrapper")
		scrapper = meteo_scrapper.MeteoScrapper()

		logging.info("Get meteo for Paris")
		sky, temperature, wind = scrapper.getMeteo("Paris")
		meteoDataList          = [sky, temperature, wind]
		logging.info("Successfully got the meteo")

		logging.info("Test the meteo data obtained")
		self.assertNotIn("", meteoDataList)
		logging.info("Meteo parameters not empty, success")


if __name__ == "__main__":
	logging.basicConfig(filename='unittests/logs/meteo_scrapper_test.log',
		level=logging.DEBUG,
		format='%(levelname)s %(relativeCreated)6d %(threadName)s %(message)s (%(module)s.%(lineno)d)',
		filemode='w')

	unittest.main()
