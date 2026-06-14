# 🔐 Password Generator - Quick Start Guide

**Get started generating secure passwords in 30 seconds!**

---

## ⚡ Quick Start

### Basic Usage (Fastest)
```bash
python password_generator.py
```

**Output:** 1 secure password (16 characters)
```
@_1Vi$r/mM2T+THb
Strength: Very Strong 💪 (7/7)
```

---

## 🎯 Common Commands

| Task | Command |
|------|---------|
| Generate 1 password | `python password_generator.py` |
| Custom length | `python password_generator.py 24` |
| 5 passwords | `python password_generator.py 20 5` |
| Interactive menu | `python password_generator_interactive.py` |

---

## 📊 What You Get

Each password includes:
- ✅ Uppercase letters (A-Z)
- ✅ Lowercase letters (a-z)
- ✅ Numbers (0-9)
- ✅ Special characters (!@#$%...)
- ✅ Strength score (0-7)
- ✅ Randomized order (no patterns)

---

## 💡 Examples

### Generate 3 passwords, 24 characters each
```bash
python password_generator.py 24 3
```

### Generate 1 extra-strong password
```bash
python password_generator.py 32
```

### Interactive mode (menu)
```bash
python password_generator_interactive.py
```
Then select options from the menu

---

## 🔒 Password Strength

| Length | Strength |
|--------|----------|
| 16 chars | Very Strong 💪 |
| 20 chars | Very Strong 💪 |
| 24 chars | Very Strong 💪 |
| 32 chars | Very Strong 💪 |

All generated passwords score **7/7** strength!

---

## 📚 Documentation

- **Full Guide:** `PASSWORD_GENERATOR_README.md`
- **Task Summary:** `PASSWORD_GENERATOR_TASK4_SUMMARY.md`
- **How It Works:** `PASSWORD_GENERATOR_README.md` (Algorithm section)

---

## 🛡️ Security Tips

1. **Use a password manager** to store passwords
2. **Never reuse** passwords across accounts
3. **Use 20+ chars** for critical accounts
4. **Don't share** passwords via email
5. **Change regularly** for sensitive accounts

---

## 📋 File Inventory

```
Password Generator/
├── password_generator.py              ← Main CLI tool
├── password_generator_interactive.py  ← Interactive menu mode
├── PASSWORD_GENERATOR_README.md       ← Full documentation
├── PASSWORD_GENERATOR_TASK4_SUMMARY.md ← Task completion summary
└── QUICKSTART.md                      ← This file
```

---

## 🚀 Next Steps

1. **Run:** `python password_generator.py`
2. **Try:** `python password_generator.py 20 5`
3. **Explore:** `python password_generator_interactive.py`
4. **Learn:** Read `PASSWORD_GENERATOR_README.md`

---

**Ready? Generate your first password! 🔐**

```bash
python password_generator.py
```
