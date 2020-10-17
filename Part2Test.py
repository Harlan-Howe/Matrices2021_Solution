import unittest
from Matrices import Matrix

A = Matrix(((1,2,3),(4,5,6),(7,8,9)))
B = Matrix(((0, 4, 6), (8, -3, 2)))
class MyTestCase(unittest.TestCase):
    def test_2_transpose(self):
        A_T = A.transpose()
        self.assertTupleEqual((3, 3),A_T.shape(),f"A transpose is wrong shape. You got {A_T.shape()}")
        self.assertTrue(A_T.equals(Matrix(((1, 4, 7),
                                  (2, 5, 8),
                                  (3, 6, 9)))), f"A transpose is incorrect. You got {A_T}")

        # TODO: Write at least two more tests to check on other matrices, perhaps non-square ones.
        # self.assertTrue(False, "You didn't write this part, did you?")
        B_T = B.transpose()
        self.assertTupleEqual((3, 2), B_T.shape(), f"B transpose is wrong shape. You got {B_T.shape()}")
        self.assertTrue(B_T.equals(Matrix(((0, 8),
                                           (4, -3),
                                           (6, 2)))), f"B transpose is incorrect. You got {B_T}")

    def test_3_double_transpose(self):
        self.assertTrue(A.transpose().transpose().equals(A), f"A^T^T should be A. You got {A.transpose().transpose()}")

        #TODO: check that your other matrices work for this, as well.
        # self.assertTrue(False, "You didn't write this part, either.")
        self.assertTrue(B.transpose().transpose().equals(B), f"B^T^T should be B. You got {B.transpose().transpose()}")


if __name__ == '__main__':
    unittest.main()
