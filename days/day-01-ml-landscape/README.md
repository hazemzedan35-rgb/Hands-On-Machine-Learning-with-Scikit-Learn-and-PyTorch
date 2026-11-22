# Day 01 — The Machine Learning Landscape

**Learning focus:** What ML is, why it is useful, and how ML systems are categorized.

[← Repository home](../../README.md) · [Starter lab](day_01_starter_lab.ipynb) · [Review exercises](exercises.md)

## 1. What is Machine Learning?

Machine Learning (ML) is a way to build computer systems that improve at a task by finding patterns in examples rather than following only hand-written rules for every situation.

A helpful way to describe an ML problem is with three parts:

| Part | Meaning | Example: spam filter |
| --- | --- | --- |
| **Task (T)** | What the system should do | Classify an email as spam or not spam |
| **Experience (E)** | What it learns from | Examples of emails and their labels |
| **Performance (P)** | How we judge its results | Accuracy, precision, recall, etc. |

A model is not "learning" in the human sense. Its training procedure adjusts parameters to improve some objective based on data.

## 2. Why use ML?

- **Hard-to-write rules:** Spam changes often; hundreds of manual rules become difficult to maintain.
- **Complex patterns:** Images and speech are difficult to describe with a few explicit instructions.
- **Changing conditions:** A system can be retrained or updated as new examples arrive.
- **Discovering patterns:** Analysis can help us notice groups or relationships in data.

**Important:** ML is not always the best option. For a simple, fixed calculation, ordinary programming may be more reliable and understandable.

## 3. Types of ML: supervision

| Type | What information it learns from | Typical use |
| --- | --- | --- |
| **Supervised** | Examples with target answers (**labels**) | Predict price (regression); classify spam (classification) |
| **Unsupervised** | Examples without target labels | Discover customer groups (clustering) |
| **Semi-supervised** | A few labeled examples plus many unlabeled ones | Train an image model with limited manual labels |
| **Self-supervised** | Prediction targets created from the data itself | Predict a masked word in a sentence |
| **Reinforcement** | Actions, states and feedback in the form of rewards | An agent learning a strategy in a game |

**Classification** predicts a category; **regression** predicts a numerical value. These are two common supervised tasks.

## 4. Batch learning versus online learning

**Batch learning:** A model is trained on a fixed dataset, deployed, and later trained again when it needs an update. Training can still use mini-batches internally; "batch" here mainly means the system is not continuously updating from incoming production examples.

**Online learning:** Training updates the model gradually from a stream or small batches of new examples. This can help with large datasets or rapidly changing data, but it requires monitoring for harmful or low-quality incoming data.

**Out-of-core learning** is a useful application of incremental training when the complete dataset cannot fit into memory.

## 5. Instance-based versus model-based

**Instance-based:** Store examples and predict by comparing a new example to known ones. *Example: k-nearest neighbors (KNN).* The similarity or distance rule matters.

**Model-based:** Fit a parameterized function or model to patterns in examples, then make predictions using it. *Example: linear regression.*

Both approaches aim for **generalization**: performing usefully on *new* examples, not merely remembering previous inputs.

## 6. My understanding checklist

- [ ] Explain task, experience and performance without reading my notes.
- [ ] Recognize classification versus regression in everyday problems.
- [ ] Decide if a problem is supervised or unsupervised.
- [ ] Explain online versus batch learning using an example.
- [ ] Run the starter notebook and change one setting.

## Next action

Complete the [short review](exercises.md), then open the [Day 01 starter lab](day_01_starter_lab.ipynb) and change the number of neighbors in the KNN classifier. Record what happens in [LEARNING-LOG](../../docs/LEARNING-LOG.md).
