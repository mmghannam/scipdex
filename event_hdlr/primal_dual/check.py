import unittest
from unittest.mock import patch
from io import StringIO

from pyscipopt import Model
import primal_dual

class TestPrimalDual(unittest.TestCase):

    model = Model()

    hdlr = primal_dual.PrimalDualEventhdlr()
    model.includeEventhdlr(hdlr, "PrimalDualEventhdlr", "User event handler for \
                                            collecting primal and dual solutions")


    def test_event_catching(self):
        self.assertEqual(len(self.model.data["primal_log"]), 1000, msg="Number of best primal solutions is incorrect")
        self.assertEqual(len(self.model.data["dual_log"]), 1000, msg="Number of best dual solutions found is incorrect.")
        pass

    def test_solution_collection(self):

        pass

    def test_pdi(self):
        pdi = primal_dual.compute_pdi(self.model.data["primal_log"], self.model.data["dual_log"])
        
        assert self.assertAlmostEqual(pdi, 10000, places=4, msg="PDI is not equal to ???") 
        pass