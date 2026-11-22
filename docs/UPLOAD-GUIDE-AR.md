# إزاي ترفع تقدمك كل يوم على GitHub؟ 🇪🇬

الدليل ده لرحلة كتاب **Hands-On Machine Learning with Scikit-Learn and PyTorch** على Windows وVS Code.

## أول مرة بس — ارفع المشروع كامل

1. فك ضغط ملف `Machine-Learning-Book-Journey.zip`، وافتح فولدر `machine-learning-book-journey` في VS Code.
2. اعمل Repository جديد من <https://github.com/new> وليكن اسمه `machine-learning-book-journey`، واختار Public. **ما تختارش Add README أو License أو .gitignore**؛ لأنهم موجودين بالفعل.
3. افتح Terminal داخل نفس فولدر المشروع في VS Code (القائمة: Terminal → New Terminal).
4. نفّذ الأوامر دي بالتتابع:

```powershell
git init
git add .
git commit -m "Initial commit: full book learning roadmap"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/machine-learning-book-journey.git
git push -u origin main
```

بدّل `YOUR_USERNAME` باسمك على GitHub. لو طلب منك تسجل دخول، اتبع شاشة تسجيل الدخول الرسمية اللي بتظهر لك. مش محتاج تبعت أي كلمة سر أو token في الشات.

لو ظهر `git is not recognized`، نزّل Git من <https://git-scm.com/downloads>، اقفل وافتح VS Code، وجرب تاني.

لو ظهر `Author identity unknown`، عرّف اسمك وإيميل Git (استخدم الإيميل اللي تفضله للـ commits):

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## كل يوم بعد المذاكرة — 4 خطوات

افتح **نفس الفولدر** ونفس الريبو على جهازك، مش Repo جديد.

**1) اعمل فولدر اليوم الجديد أوتوماتيك:**

```powershell
python scripts/journey.py new --chapter 2 --title "Working with Real Data"
```

هتلاقي فولدر جديد باسم شبه `days/day-03-working-with-real-data/`. الأمر بيزود اليوم تلقائيًا، ويحدّث جدول التقدم في README وملف سجل الأيام. لو عايز Notebook فاضي تضيفه لليوم ده، زود `--notebook` في آخر نفس الأمر.

**2) افتح `README.md` بتاع اليوم واكتب اللي فهمته:**

اقرأ → اكتب بإسلوبك → جاوب التمارين → جرّب كود لو مناسب. مش لازم تخلص فصل كامل في يوم. بعد ما تخلص النوتس شغّل:

```powershell
python scripts/journey.py mark --day 3 --status notes
```

ولو خلصت هدف اليوم النظري والعملي فعلًا، ممكن تستخدم `--status complete`. الرقم بيتغير حسب رقم اليوم.

**3) ارفع كل التعديلات:**

```powershell
git add .
git commit -m "Day 3: notes on working with real data"
git push
```

**4) افتح Repo GitHub واعمل Refresh:** هتلاقي التعديلات والملفات الجديدة ظهرت في نفس الريبو.

### في اليوم الرابع مثلًا

```powershell
python scripts/journey.py new --chapter 2 --title "Train Test Split" --notebook
# اكتب النوتس والكود في الملفات الجديدة
python scripts/journey.py mark --day 4 --status notes
git add .
git commit -m "Day 4: train test split practice"
git push
```

## لما تخلص فصل كامل

```powershell
python scripts/journey.py chapter --chapter 1 --status complete
git add .
git commit -m "Complete chapter 1"
git push
```

ما تعملش كده إلا لما تكون خلصت الفصل فعلًا.

## لو مش عايز تستخدم Terminal

تقدر تعدّل `README.md` بتاع أي يوم من GitHub بعلامة القلم ثم **Commit changes**. ولإنشاء يوم جديد من المتصفح: اختار **Add file → Create new file** واكتب اسم زي `days/day-03-new-topic/README.md`، واكتب نوتس اليوم ثم **Commit changes**. لكن طريقة المتصفح دي **مش هتحدّث جدول التقدم أوتوماتيك**؛ لازم تعدّل الجدول يدويًا أو تشغل السكريبت على جهازك وبعدها ترفع الملفات.

## لو واجهتك مشكلة

- `nothing to commit`: مفيش تعديلات جديدة محفوظة.
- `git push` rejected: ممكن فيه تغييرات اتعملت على GitHub من مكان تاني؛ لو مفيش تعارض، جرّب `git pull --rebase origin main` ثم `git push`.
- لا ترفع `.venv/` أو مفاتيح API أو أي بيانات خاصة؛ `.gitignore` بيستبعد الملفات الشائعة دي.
- ملفات `.ipynb` ممكن تكون كبيرة؛ خلي بيانات التدريب الضخمة بره الريبو.

**الفكرة:** كل يوم تعديل جديد + Commit جديد على **نفس الريبو**؛ GitHub History هيوثق رحلتك من البداية للنهاية.
