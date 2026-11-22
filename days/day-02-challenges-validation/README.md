# Day 02 — ML Challenges and Validation

**Learning focus:** Why an ML system may fail and how to evaluate it fairly.

[← Repository home](../../README.md) · [Starter lab](day_02_starter_lab.ipynb) · [Review exercises](exercises.md)

## 1. Two broad sources of problems

### Problems with data

| Challenge | What can happen | Possible response |
| --- | --- | --- |
| **Too little useful data** | The model cannot learn a reliable pattern | Gather more relevant examples, use an appropriate simpler model |
| **Nonrepresentative sample** | Model performs well on collected samples but poorly for the real population | Improve sampling; check training versus deployment populations |
| **Low-quality data** | Errors, noisy measurements or incorrect labels mislead training | Review and correct data quality issues |
| **Unhelpful features** | Inputs do not contain useful information for the task | Choose or create meaningful features with domain knowledge |

Not *every* ML problem needs an enormous dataset: the amount depends on the model, problem difficulty, noise and existing knowledge.

### Problems with models

**Overfitting (often associated with high variance):** The model matches details of training data, including accidental noise, but performs noticeably worse on new examples.

Possible solutions: add more representative training data, use a simpler model, tune regularization, reduce irrelevant noise, or choose better features.

**Underfitting (often associated with high bias):** The model is too restricted or misses the important structure, so even training performance is poor.

Possible solutions: use a more flexible model, add meaningful features, or reduce excessive regularization.

These patterns are useful intuition, not perfect diagnostic laws: real-world issues can overlap.

## 2. Training, validation and test sets

| Split | Purpose | What **not** to do |
| --- | --- | --- |
| **Training set** | Fit model parameters | Treat its score as final evidence of performance |
| **Validation set** | Compare models and select hyperparameters | Keep tuning until the separate test score looks good |
| **Test set** | Make a final estimate of performance on unseen examples | Use it repeatedly to select models |

**Mental model:**

```text
Dataset
  ├── Development data
  │   ├── Training split   → learn parameters
  │   └── Validation split → choose model / hyperparameters
  └── Held-out test split  → evaluate once at the end
```

A test score estimates performance for examples similar to the test population. It is not a guarantee about every future situation.

## 3. k-fold cross-validation

With `k=5`:

1. Divide *development/training* data into 5 folds.
2. Train using 4 folds and evaluate on the remaining fold.
3. Repeat so each fold is used for validation once.
4. Average the validation scores to compare candidate settings.
5. Fit the selected model on the available development data and evaluate on the untouched test set.

Cross-validation often uses limited data more efficiently than one fixed validation split. The correct fold strategy matters: time-series data, repeated samples from one person, and grouped measurements may need specialized splits instead of random folds.

## 4. An important extra risk: data leakage

**Data leakage** happens when information not genuinely available at prediction time influences model development or training. It makes evaluation seem better than reality.

For example, if you compute a data transformation using *all* examples before the train/test split, information from the test set may leak into the model. A scikit-learn **Pipeline** can help fit transformations using only the relevant training portion.

## 5. My understanding checklist

- [ ] Explain overfitting versus underfitting with an example.
- [ ] Explain why test data must remain untouched during tuning.
- [ ] Describe how 5-fold cross-validation works.
- [ ] Recognize sampling bias and data leakage.
- [ ] Run the notebook and compare training and validation error.

## Next action

Use the [Day 02 starter lab](day_02_starter_lab.ipynb) to experiment with a simple curve-fitting problem and model selection by cross-validation. Answer the [review exercises](exercises.md) in your own words.
