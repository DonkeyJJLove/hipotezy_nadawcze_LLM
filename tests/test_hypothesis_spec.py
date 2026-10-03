from dataclasses import replace
import importlib.util,json,pathlib,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("hypothesis_spec",ROOT/"contracts/hypothesis_spec.py")
m=importlib.util.module_from_spec(spec);sys.modules["hypothesis_spec"]=m;spec.loader.exec_module(m)
class HypothesisSpecTests(unittest.TestCase):
 def load(self):return json.loads((ROOT/"examples/falsification_fixture.json").read_text())
 def test_fixture_is_testable_not_result(self):
  x=self.load();h=m.HypothesisSpec(**{**x["hypothesis"],"assumptions":tuple(x["hypothesis"]["assumptions"]),"observable_consequences":tuple(x["hypothesis"]["observable_consequences"]),"falsifiers":tuple(x["hypothesis"]["falsifiers"]),"evidence_refs":tuple(x["hypothesis"]["evidence_refs"])}).validate()
  self.assertEqual(h.status,"TESTABLE");self.assertEqual(h.authority_effect,"NONE")
 def test_confirmed_without_evidence_denied(self):
  x=self.load()["hypothesis"];x["status"]="CONFIRMED";x["digest"]=""
  h=m.HypothesisSpec(**{**x,"assumptions":tuple(x["assumptions"]),"observable_consequences":tuple(x["observable_consequences"]),"falsifiers":tuple(x["falsifiers"]),"evidence_refs":()})
  with self.assertRaises(m.HypothesisContractError):h.sealed()
 def test_experiment_is_non_effectful_and_has_machine_falsifier(self):
  x=self.load()["experiment"];e=m.ExperimentSpec(**{**x,"falsifier_refs":tuple(x["falsifier_refs"])}).validate()
  self.assertEqual((e.authority_effect,e.execution_effect),("NONE","NONE"));self.assertTrue(e.falsifier_refs)
if __name__=="__main__":unittest.main()
