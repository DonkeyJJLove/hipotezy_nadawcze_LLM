from __future__ import annotations
from dataclasses import asdict,dataclass,replace
from hashlib import sha256
import json,re
from typing import Mapping,Any
SHA=re.compile(r"^[0-9a-f]{64}$");ID=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$")
class HypothesisContractError(ValueError):pass
def canon(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def ref(v,n):
 if not isinstance(v,str) or ID.fullmatch(v) is None:raise HypothesisContractError(n)
 return v
def texts(v,n,empty=False):
 if not isinstance(v,(list,tuple)) or (not empty and not v) or any(not isinstance(x,str) or not x.strip() for x in v):raise HypothesisContractError(n)
 o=tuple(v)
 if len(o)!=len(set(o)):raise HypothesisContractError(n)
 return o
@dataclass(frozen=True)
class HypothesisSpec:
 hypothesis_id:str;claim:str;assumptions:tuple[str,...];observable_consequences:tuple[str,...];falsifiers:tuple[str,...];evidence_refs:tuple[str,...];status:str="HYPOTHESIS";authority_effect:str="NONE";digest:str=""
 def payload(self):d=asdict(self);d.pop("digest",None);return d
 def compute(self):return sha256(b"LION/HYPOTHESIS/1\0"+canon(self.payload())).hexdigest()
 def validate(self,req=True):
  ref(self.hypothesis_id,"hypothesis_id")
  if not isinstance(self.claim,str) or not self.claim.strip():raise HypothesisContractError("claim")
  texts(self.assumptions,"assumptions");texts(self.observable_consequences,"observable_consequences");texts(self.falsifiers,"falsifiers");texts(self.evidence_refs,"evidence_refs",True)
  if self.status not in {"HYPOTHESIS","TESTABLE","SUPPORTED","FALSIFIED","SUPERSEDED","CONFIRMED"}:raise HypothesisContractError("status")
  if self.status in {"SUPPORTED","CONFIRMED"} and not self.evidence_refs:raise HypothesisContractError("evidence required")
  if self.authority_effect!="NONE":raise HypothesisContractError("authority")
  if req and (not SHA.fullmatch(self.digest) or self.digest!=self.compute()):raise HypothesisContractError("digest")
  return self
 def sealed(self):return replace(self,digest=self.compute()).validate()
@dataclass(frozen=True)
class ExperimentSpec:
 experiment_id:str;hypothesis_ref:str;input_schema_ref:str;output_schema_ref:str;falsifier_refs:tuple[str,...];risk_bound:str;authority_effect:str="NONE";execution_effect:str="NONE";digest:str=""
 def payload(self):d=asdict(self);d.pop("digest",None);return d
 def compute(self):return sha256(b"LION/EXPERIMENT/1\0"+canon(self.payload())).hexdigest()
 def validate(self,req=True):
  for v,n in [(self.experiment_id,"experiment_id"),(self.hypothesis_ref,"hypothesis_ref"),(self.input_schema_ref,"input_schema_ref"),(self.output_schema_ref,"output_schema_ref")]:ref(v,n)
  texts(self.falsifier_refs,"falsifier_refs")
  if not isinstance(self.risk_bound,str) or not self.risk_bound.strip():raise HypothesisContractError("risk_bound")
  if self.authority_effect!="NONE" or self.execution_effect!="NONE":raise HypothesisContractError("effects")
  if req and (not SHA.fullmatch(self.digest) or self.digest!=self.compute()):raise HypothesisContractError("digest")
  return self
 def sealed(self):return replace(self,digest=self.compute()).validate()
