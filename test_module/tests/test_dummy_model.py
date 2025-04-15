from odoo.tests.common import TransactionCase

class TestDummyModel(TransactionCase):
    def setUp(self):
        super(TestDummyModel, self).setUp()
        # Create a dummy record in the model.
        # Note: In order for this to work, your module must be installed.
        self.dummy = self.env['dummy.model'].create({'name': 'Test Dummy'})

    def test_compute_something(self):
        """Test that compute_something returns (3, [6,7,8,9]) correctly."""
        result = self.dummy.compute_something()
        # 1+2 should equal 3.
        self.assertEqual(result[0], 3)
        # List comprehension yields [6,7,8,9] because these are the items >5 in range(10).
        self.assertEqual(result[1], [6, 7, 8, 9])

    def test_method_without_self_error(self):
        """Test that calling method_without_self raises a TypeError because it lacks 'self'."""
        # When calling a model method that lacks the 'self' parameter,
        # Python should raise a TypeError.
        with self.assertRaises(TypeError):
            self.dummy.method_without_self()
