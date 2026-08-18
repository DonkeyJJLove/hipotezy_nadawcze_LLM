# hipotezy_nadawcze_LLM — AI-Native Enterprise Roadmap

Enterprise role: **Epistemic Hypothesis Lab**.

This repository should remain deliberately small. Its purpose is to formulate narrow hypotheses about LLM representation/communication, define how they could be falsified, preserve evidence for and against, and export validated research records into the wider R&D system.

## Current strength

The existing text→token work already uses a useful pattern:

```text
formal claim
→ observable consequences
→ falsification conditions
→ theoretical/empirical argument
→ probability/confidence estimate
```

The roadmap makes this structure machine-readable and prevents a hypothesis from becoming a production rule merely because it is persuasive.

## Phase 1 — HypothesisSpec

Create a versioned contract:

```text
HypothesisSpec {
  hypothesis_id,
  title,
  claim,
  scope,
  observable_consequences,
  falsifiers,
  evidence_for,
  evidence_against,
  alternative_explanations,
  confidence,
  confidence_basis,
  epistemic_status,
  created_at,
  updated_at,
  supersedes
}
```

## Phase 2 — ExperimentSpec

Each serious hypothesis may link to reproducible experiments:

```text
experiment_id
hypothesis_id
model/provider/version
inputs/test-set refs
method
expected falsifying result
seed/config where relevant
result artifact/hash
limitations
```

Negative results are first-class outputs.

## Phase 3 — explicit confidence status

A number such as `0.90` must identify its basis:

```text
subjective_prior
expert_judgment
calibrated_model
empirical_frequency
posterior_estimate
```

Do not present one class as another.

## Phase 4 — multi-agent falsification cell

For higher-value hypotheses separate roles:

```text
Hypothesis Generator
Evidence Collector
Falsification Agent
Alternative-Explanation Agent
Methodology Auditor
```

A model should not be the only validator of a hypothesis about its own behavior.

## Phase 5 — writeups R&D adapter

Export stable records to `writeups` as ResearchRecord references:

```text
HypothesisSpec
→ ExperimentResult
→ R&D ResearchRecord
→ engineering candidate only if justified
```

Link to the canonical hypothesis rather than copying and silently editing it.

## Phase 6 — Cyber-Lion evidence interface

Expose read-only capabilities:

```text
hypothesis.list
hypothesis.read
hypothesis.evidence.export
experiment.result.read
```

Research agents may consume these records, but runtime policy does not import them as authority.

## Phase 7 — supersession and contradiction

Support explicit states:

```text
ACTIVE
WEAKENED
FALSIFIED
SUPPORTED
SUPERSEDED
```

Conflicting evidence remains attached to the same hypothesis lineage.

## Required tests / checks

- missing falsifier → hypothesis cannot be marked formal;
- confidence with no basis → reject;
- evidence source missing → retain as unsupported claim, not observation;
- same hypothesis ID with changed claim → require new version/supersession;
- negative result cannot be deleted by promotion;
- model-version drift remains visible.

## Do not do

```text
model explanation == validation
analogy == empirical evidence
high confidence == normative rule
textual elegance == truth
simulation/result from one model == global LLM property
```

## Enterprise references

R&D operating model:

`https://github.com/DonkeyJJLove/ai_platform/blob/master/cyber_lion/enterprise/RND_OPERATING_MODEL.md`

R&D narrative:

`https://github.com/DonkeyJJLove/writeups/blob/master/AI_NATIVE_ENTERPRISE_RND_WRITEUP.md`
