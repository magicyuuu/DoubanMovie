# -*- coding: UTF-8 -*-
__author__ = 'yushiwei'

import unittest
import logging
import logging.config
import douban

class testDouban(unittest.TestCase):

    def setUp(self):
        self.logging = logging.getLogger()
        logging.config.fileConfig('../conf/logging.dev.conf')

    def tearDown(self):
        pass

    def testSearchMovie(self):
        result = douban.searchMovie('')
        self.assertTrue(result == {})

        result = douban.searchMovie(None)
        self.assertTrue(result == {})

        result = douban.searchMovie('d')
        self.assertTrue(result == {})

        result = douban.searchMovie('章子怡')

        result = douban.searchMovie('教父')

