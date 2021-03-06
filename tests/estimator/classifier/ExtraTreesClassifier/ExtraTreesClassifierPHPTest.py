# -*- coding: utf-8 -*-

import unittest

from sklearn.ensemble import ExtraTreesClassifier

from tests.estimator.classifier.Classifier import Classifier
from tests.language.PHP import PHP


class ExtraTreesClassifierPHPTest(PHP, Classifier, unittest.TestCase):

    def setUp(self):
        super(ExtraTreesClassifierPHPTest, self).setUp()
        self.estimator = ExtraTreesClassifier(random_state=0)

    def tearDown(self):
        super(ExtraTreesClassifierPHPTest, self).tearDown()

    @unittest.skip('The generated code would be too large.')
    def test_existing_features_w_digits_data(self):
        pass

    @unittest.skip('The generated code would be too large.')
    def test_random_features_w_digits_data(self):
        pass
