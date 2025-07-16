from LinearClassifier import Perceptron
import unittest
import numpy as np

class TestPerceptron(unittest.TestCase):
    
    def setUp(self):
        pass

    def extract_loss_values(self, loss_history):
        # Update this if the loss_history format has changed
        loss_values = []
        for entry in loss_history:
            if isinstance(entry, dict) and 'percent_wrong' in entry:
                loss_values.append(entry['percent_wrong'])
            elif isinstance(entry, tuple):
                loss_values.append(entry[0])
            else:
                loss_values.append(entry)
        return loss_values

    def test_basic_linearly_separable_data(self):
        perceptron = Perceptron(2)
        data = [([1, 1], 1), ([2, 2], 1), ([3, 3], 1), ([-1, -1], -1), ([-2, -2], -1), ([-3, -3], -1)]
        perceptron.fit(data, 100)
        loss_values = self.extract_loss_values(perceptron.loss_history)
        self.assertEqual(loss_values[-1], 0)
        self.assertEqual(perceptron.predict([1, 1]), 1)
        self.assertEqual(perceptron.predict([-1, -1]), -1)
        self.assertIsNotNone(perceptron.theta)
        self.assertIsNotNone(perceptron.thetaZero)

    def test_xor_problem_non_convergence(self):
        perceptron = Perceptron(2)
        xor_data = [([0, 0], -1), ([0, 1], 1), ([1, 0], 1), ([1, 1], -1)]
        perceptron.fit(xor_data, 100)
        loss_values = self.extract_loss_values(perceptron.loss_history)
        self.assertGreater(loss_values[-1], 0)

    def test_single_dimension_data(self):
        perceptron = Perceptron(1)
        data_1d = [([2], 1), ([3], 1), ([4], 1), ([-1], -1), ([-2], -1), ([-3], -1)]
        perceptron.fit(data_1d, 50)
        loss_values = self.extract_loss_values(perceptron.loss_history)
        self.assertEqual(loss_values[-1], 0)
        self.assertEqual(perceptron.predict([1]), 1)
        self.assertEqual(perceptron.predict([-1]), -1)
        self.assertEqual(len(perceptron.theta), 1)

    def test_different_line_orientation(self):
        perceptron = Perceptron(2)
        alt_data = [([0, 2], 1), ([1, 1], 1), ([2, 0], 1), ([0, 0], -1), ([1, -1], -1), ([2, -2], -1)]
        perceptron.fit(alt_data, 100)
        loss_values = self.extract_loss_values(perceptron.loss_history)
        self.assertEqual(loss_values[-1], 0)
        self.assertEqual(perceptron.predict([0, 2]), 1)
        self.assertEqual(perceptron.predict([2, -2]), -1)

    def test_all_positive_labels(self):
        perceptron = Perceptron(2)
        pos_data = [([1, 1], 1), ([2, 2], 1), ([3, 3], 1), ([0, 1], 1), ([1, 0], 1)]
        perceptron.fit(pos_data, 50)
        loss_values = self.extract_loss_values(perceptron.loss_history)
        self.assertEqual(loss_values[-1], 0)
        for point, _ in pos_data:
            self.assertEqual(perceptron.predict(point), 1)

    def test_convergence_analysis(self):
        perceptron = Perceptron(2)
        conv_data = [([1, 2], 1), ([2, 1], 1), ([2, 3], 1), ([-1, -1], -1), ([-2, -1], -1), ([-1, -2], -1)]
        perceptron.fit(conv_data, 200)
        loss_values = self.extract_loss_values(perceptron.loss_history)
        self.assertEqual(loss_values[-1], 0)
        epochs = len([entry for entry in perceptron.loss_history if isinstance(entry, dict)])
        self.assertGreater(epochs, 0)
        self.assertLess(epochs, 200)

    def test_training_examples_classification(self):
        perceptron = Perceptron(2)
        verify_data = [([1, 1], 1), ([2, 2], 1), ([3, 3], 1), ([-1, -1], -1), ([-2, -2], -1), ([-3, -3], -1)]
        perceptron.fit(verify_data, 100)
        for point, expected in verify_data:
            predicted = perceptron.predict(point)
            self.assertEqual(predicted, expected)

    def test_boundary_predictions(self):
        perceptron = Perceptron(2)
        boundary_data = [([1, 1], 1), ([2, 2], 1), ([-1, -1], -1), ([-2, -2], -1)]
        perceptron.fit(boundary_data, 100)
        test_points = [[0, 0], [0.1, 0.1], [-0.1, -0.1], [0.5, 0.5], [-0.5, -0.5]]
        for point in test_points:
            prediction = perceptron.predict(point)
            self.assertIn(prediction, [-1, 1])

    def test_initialization(self):
        perceptron = Perceptron(3)
        self.assertEqual(perceptron.thetaZero, 0.0)
        self.assertEqual(len(perceptron.theta), 3)
        self.assertTrue(np.array_equal(perceptron.theta, np.zeros(3)))

    def test_predict_method(self):
        perceptron = Perceptron(2)
        perceptron.theta = np.array([1, 1])
        perceptron.thetaZero = 0
        self.assertEqual(perceptron.predict([1, 1]), 1)
        self.assertEqual(perceptron.predict([-1, -1]), -1)
        self.assertEqual(perceptron.predict([0, 0]), -1)

    def test_loss_history_structure(self):
        perceptron = Perceptron(2)
        data = [([1, 1], 1), ([2, 2], 1), ([-1, -1], -1), ([-2, -2], -1)]
        perceptron.fit(data, 10)
        self.assertIsNotNone(perceptron.loss_history)
        self.assertGreater(len(perceptron.loss_history), 0)
        dict_entries = [entry for entry in perceptron.loss_history if isinstance(entry, dict)]
        for entry in dict_entries:
            self.assertIn('percent_wrong', entry)
            self.assertIn('epoch', entry)
            self.assertIn('theta', entry)
            self.assertIn('thetaZero', entry)

    def test_empty_data_handling(self):
        perceptron = Perceptron(2)
        try:
            perceptron.fit([], 10)
        except Exception as e:
            self.assertIsInstance(e, (ValueError, IndexError, ZeroDivisionError))

    def test_parameter_updates(self):
        perceptron = Perceptron(2)
        data = [([1, 1], 1), ([-1, -1], -1)]
        initial_theta = perceptron.theta.copy()
        initial_thetaZero = perceptron.thetaZero
        perceptron.fit(data, 10)
        theta_changed = not np.array_equal(perceptron.theta, initial_theta)
        thetaZero_changed = perceptron.thetaZero != initial_thetaZero
        self.assertTrue(theta_changed or thetaZero_changed)

if __name__ == '__main__':
    unittest.main(verbosity=2)
