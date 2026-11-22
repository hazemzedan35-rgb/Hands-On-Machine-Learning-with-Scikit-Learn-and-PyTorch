# 📘 Hands-On Machine Learning — My Learning Journey

**From the first ML concept to deep learning — learning, practicing, and documenting one session at a time.**

This repository is my **personal study journal** while working through *Hands-On Machine Learning with Scikit-Learn and PyTorch* by **Aurélien Géron**. The goal is to document a complete journey through the book, including Scikit-Learn, neural networks, and PyTorch — not just a two-day project.

**Progress tracking:** See the live tables below. My first two study sessions cover material from Chapter 1; their notebooks are **optional starter labs**, not automatically completed practice. Future chapter folders are placeholders until I study them.

> ✅ = completed by me · 📝 = notes documented · 🧪 = prepared practice · ⏳ = not started / planned. I update this honestly as I learn.

## 📊 Book roadmap — all 19 chapters

<!-- CHAPTERS:START -->
| Chapter | Topic | Status | Logged sessions |
| --- | --- | --- | ---: |
| 01 | [The Machine Learning Landscape](chapters/01-the-machine-learning-landscape/README.md) | 📝 In progress | 2 |
| 02 | [End-to-End Machine Learning Project](chapters/02-end-to-end-machine-learning-project/README.md) | ⏳ Not started | 0 |
| 03 | [Classification](chapters/03-classification/README.md) | ⏳ Not started | 0 |
| 04 | [Training Models](chapters/04-training-models/README.md) | ⏳ Not started | 0 |
| 05 | [Decision Trees](chapters/05-decision-trees/README.md) | ⏳ Not started | 0 |
| 06 | [Ensemble Learning and Random Forests](chapters/06-ensemble-learning-and-random-forests/README.md) | ⏳ Not started | 0 |
| 07 | [Dimensionality Reduction](chapters/07-dimensionality-reduction/README.md) | ⏳ Not started | 0 |
| 08 | [Unsupervised Learning Techniques](chapters/08-unsupervised-learning-techniques/README.md) | ⏳ Not started | 0 |
| 09 | [Introduction to Artificial Neural Networks](chapters/09-introduction-to-artificial-neural-networks/README.md) | ⏳ Not started | 0 |
| 10 | [Building Neural Networks with PyTorch](chapters/10-building-neural-networks-with-pytorch/README.md) | ⏳ Not started | 0 |
| 11 | [Training Deep Neural Networks](chapters/11-training-deep-neural-networks/README.md) | ⏳ Not started | 0 |
| 12 | [Deep Computer Vision Using Convolutional Neural Networks](chapters/12-deep-computer-vision-using-convolutional-neural-networks/README.md) | ⏳ Not started | 0 |
| 13 | [Processing Sequences Using RNNs and CNNs](chapters/13-processing-sequences-using-rnns-and-cnns/README.md) | ⏳ Not started | 0 |
| 14 | [Natural Language Processing with RNNs and Attention](chapters/14-natural-language-processing-with-rnns-and-attention/README.md) | ⏳ Not started | 0 |
| 15 | [Transformers for Natural Language Processing and Chatbots](chapters/15-transformers-for-natural-language-processing-and-chatbots/README.md) | ⏳ Not started | 0 |
| 16 | [Vision and Multimodal Transformers](chapters/16-vision-and-multimodal-transformers/README.md) | ⏳ Not started | 0 |
| 17 | [Speeding Up Transformers](chapters/17-speeding-up-transformers/README.md) | ⏳ Not started | 0 |
| 18 | [Autoencoders, GANs, and Diffusion Models](chapters/18-autoencoders-gans-and-diffusion-models/README.md) | ⏳ Not started | 0 |
| 19 | [Reinforcement Learning](chapters/19-reinforcement-learning/README.md) | ⏳ Not started | 0 |
<!-- CHAPTERS:END -->

The roadmap also includes the book's appendices: [Appendices A–F](docs/ROADMAP.md#appendices). Some appendices are published online by the author.

## 📅 My learning days

A chapter may take **several days**. I create one folder per study session, so my pace is flexible rather than being forced into exactly 19 days.

<!-- DAYS:START -->
| Day | Chapter | Topic | Progress |
| --- | --- | --- | --- |
| 01 | 01 | [ML Landscape and Learning Systems](days/day-01-ml-landscape/README.md) | 📝 Notes written |
| 02 | 01 | [ML Challenges and Validation](days/day-02-challenges-validation/README.md) | 📝 Notes written |
<!-- DAYS:END -->

## 🔁 How I update this repository each day

**Step 1 — Create the next day automatically:**

```bash
python scripts/journey.py new --chapter 2 --title "Working with Real Data"
```

The command creates `days/day-03-working-with-real-data/` with note and exercise templates, and updates the tables on this page. Add `--notebook` if you want an empty Jupyter notebook for an experiment.

**Step 2 — Study and edit:** Write the main concepts **in my own words** inside that day's `README.md`, answer `exercises.md`, and add code when appropriate.

**Step 3 — Mark my actual progress:**

```bash
python scripts/journey.py mark --day 3 --status notes
# or: --status complete (only when the day's own goals are finished)
```

**Step 4 — Save changes on GitHub:**

```bash
git add .
git commit -m "Day 3: working with real data"
git push
```

Start with the [**daily upload guide in Arabic**](docs/UPLOAD-GUIDE-AR.md), which explains initial setup and all daily updates from Windows. You can also update Markdown through GitHub's website.

## 📁 Folder structure

```text
machine-learning-book-journey/
├── README.md                    # Live dashboard + quick instructions
├── chapters/                    # 19 book-chapter workspaces (not prefilled study notes)
│   ├── 01-the-machine-learning-landscape/
│   ├── 02-end-to-end-machine-learning-project/
│   └── ... through chapter 19
├── appendices/                  # Appendices A–F (optional/online)
├── days/                        # Day 01, Day 02, and your future daily notes
│   ├── day-01-ml-landscape/
│   ├── day-02-challenges-validation/
│   └── day-03-.../              # Automatically created when you study
├── docs/
│   ├── ROADMAP.md               # Complete book structure
│   ├── LEARNING-LOG.md          # Learning journal
│   ├── UPLOAD-GUIDE-AR.md       # Daily GitHub steps (Arabic)
│   └── progress.json            # Tracking data (updated by helper script)
├── templates/                   # Daily notes and review templates
├── scripts/journey.py           # Make a day, update status, mark a chapter
├── requirements.txt
└── .github/workflows/validate.yml
```

## 🧪 My practice routine

1. **Understand:** Explain the idea without copying the book.
2. **Apply:** Try a short experiment if it helps.
3. **Evaluate:** What worked? How do I know? Where could it fail?
4. **Reflect:** Write the takeaway and one thing still confusing.
5. **Commit:** Save the day's progress in Git history.

The first two prepared notebooks use local/generated data. For those notebooks:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

The Python helper script works with the standard library, so it does **not** require installing the notebook dependencies. Future PyTorch chapters may need extra libraries, which I will add only as needed.

## 🔗 Official resources and credits

- [Book details and table of contents (O'Reilly)](https://www.oreilly.com/library/view/hands-on-machine-learning/9798341607972/)
- [Author's site](https://ageron.github.io/)
- [Author's official code examples](https://github.com/ageron/handson-mlp)

This is an **independent study journal**, not an official book repository or a copy of the author's notebooks. All future study notes, examples and exercises should be my own work. No copyrighted book chapters or full exercise solutions are included.

## 📄 License

My original repository code and learning materials are under the [MIT License](LICENSE). Book text, illustrations, and the author's code have their own rights and licenses.
