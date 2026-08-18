# LLM Hypothesis Lab — Process Guard

This repository is a falsification laboratory. Its main failure mode is converting an elegant explanatory model into a fact without enough evidence.

## Required structure for every hypothesis

```text
TEZA
→ observable consequences
→ falsifier
→ evidence for
→ evidence against
→ alternative explanations
→ confidence
→ next experiment
```

## Invariants

- hypothesis language must remain separate from established fact;
- a model-generated explanation is not evidence for itself;
- negative results are retained rather than rewritten away;
- probability estimates must identify whether they are measured, calibrated or subjective;
- textual / semantic structure can be analyzed as a signal, but it is not direct evidence of hidden internal model state unless independently validated.

## `_neuro` / EEG-like interpretation

Use only as a process metaphor:

```text
baseline = current accepted hypothesis state
burst    = rapid emergence of explanatory links
coupling = several hypotheses sharing the same evidence source
 drift   = confidence grows without new independent evidence
recovery = falsification / confidence correction
```

## Review loop

```text
claim
→ source map
→ counter-hypothesis
→ test
→ update confidence
→ preserve rejected path
→ publish status
```

The goal is not to protect a hypothesis. The goal is to make it increasingly difficult for a false hypothesis to survive.
