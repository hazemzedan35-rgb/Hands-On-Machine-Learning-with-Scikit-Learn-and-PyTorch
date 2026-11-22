# Day 02 — Self-check exercises

These are original questions intended for active recall.

1. A model gets 99% accuracy on training data and 62% on validation data. What might be happening? Name two possible solutions.
2. Both training and validation errors are large. What does this suggest, and what would you try next?
3. Why is it dangerous to compare twenty models on a test set and then report only the highest test score?
4. A model predicts crop conditions in multiple regions, but all training samples are from one farm. Which data challenge is most obvious?
5. Explain 5-fold cross-validation in two sentences, without using the word "magic".
6. A weather model uses tomorrow's observed rainfall to predict tomorrow's rainfall. Why is this evaluation invalid for a real forecast?
7. A dataset has several observations from each individual. Why might a random row split be misleading?

## Notebook experiment

Change the list of polynomial degrees and compare:

- Training error versus validation error.
- The cross-validation average error for each candidate.
- The final test error, which should be checked only after choosing the best candidate.

**Reflection:** Did the most complicated model win? Why or why not?

Answer independently first; then revisit your notes and discuss any uncertain answers.
