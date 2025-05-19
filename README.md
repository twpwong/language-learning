# Learning

This repository contains small experiments for language learning tools.

## Japanese Conjugation

`japanese_conjugation.py` provides minimal utilities for classifying and conjugating Japanese verbs. It defines a set `GODAN_RU_EXCEPTIONS` listing verbs ending with **る** that are conjugated as godan verbs (e.g. `切る`, `走る`, `入る`). These verbs are detected in `classify_verb`.

Example:

```python
>>> import japanese_conjugation as jc
>>> jc.classify_verb("切る")
'godan'
>>> jc.conjugate("切る", "masu")
'切ります'
```
