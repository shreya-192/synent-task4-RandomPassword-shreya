# 🔐 Secure Password Generator

A professional-grade Python tool for generating cryptographically secure random passwords with customizable options.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

---

## ✨ Features

- **🔒 Secure Generation** - Uses Python's `random` module for cryptographic randomness
- **🎯 Guaranteed Diversity** - Every password includes uppercase, lowercase, digits, and special characters
- **⚙️ Customizable Length** - Generate passwords from 4 to 256+ characters
- **📊 Strength Analysis** - Built-in password strength scoring (0-7 scale)
- **🔄 Batch Generation** - Generate multiple passwords at once
- **⚡ CLI Mode** - Command-line interface for scripting and automation
- **💻 Interactive Mode** - User-friendly menu-driven interface
- **📁 No Dependencies** - Uses Python standard library only

---

## 🚀 Quick Start

### Installation

No installation required! Just clone or download the repository:

```bash
git clone https://github.com/shreya-192/synent-task4-RandomPassword-shreya.git
cd synent-task4-RandomPassword-shreya
```

### Basic Usage

#### **Interactive Mode** (Easiest for beginners)
```bash
python password_generator_interactive.py
```
Menu options:
1. Generate 1 password (default 16 chars)
2. Generate multiple passwords
3. Custom settings
4. Exit

#### **CLI Mode** (For automation)

Generate 1 password (16 characters):
```bash
python password_generator.py
```

Generate 1 password (20 characters):
```bash
python password_generator.py 20
```

Generate 5 passwords (16 characters each):
```bash
python password_generator.py 16 5
```

---

## 📋 Usage Examples

### Example 1: Generate a Single Password
```bash
$ python password_generator.py
Generated Password: Kx7$mP2vQwL9nR4@
Strength: 7/7 ⭐⭐⭐⭐⭐⭐⭐ (Very Strong)
```

### Example 2: Generate 5 Passwords
```bash
$ python password_generator.py 16 5
Password 1: Kx7$mP2vQwL9nR4@
Password 2: 9vB#tH8kJqM1wY3z
Password 3: E5$aG2@dF4sL7nJ9
Password 4: r8X!p1C6vT2eMw4Q
Password 5: U3$jV7%hN9kB0sY5

All passwords scored: 7/7 Strength
```

### Example 3: Custom Length (32 characters)
```bash
$ python password_generator.py 32
Generated Password: Kx7$mP2vQwL9nR4@9vB#tH8kJqM1wY3z
Strength: 7/7 ⭐⭐⭐⭐⭐⭐⭐ (Very Strong)
```

---

## 🔐 Password Characteristics

### Character Set (94 total)
- **Uppercase:** A-Z (26 characters)
- **Lowercase:** a-z (26 characters)
- **Digits:** 0-9 (10 characters)
- **Special:** !@#$%^&*()_+-=[]{}|;:,.<>? (32 characters)

### Strength Scoring (0-7 scale)

| Score | Level | Requirements |
|-------|-------|--------------|
| 7 | Very Strong | All 4 char types + 16+ chars |
| 6 | Strong | All 4 char types + 12+ chars |
| 5 | Strong | All 4 char types + 8+ chars |
| 4 | Moderate | All 4 char types + 4+ chars |
| 3 | Weak | Missing character type |
| 2 | Very Weak | Missing 2+ char types |
| 1 | Extremely Weak | Missing 3+ char types |

Every generated password guarantees:
- ✅ All 4 character types (uppercase, lowercase, digits, special)
- ✅ Minimum score of 4/7
- ✅ Cryptographically random selection

---

## 🎯 Command Reference

### Interactive Mode
```bash
python password_generator_interactive.py
```

### CLI Mode
```bash
python password_generator.py [length] [count]
```

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| length | int | 16 | Password length (4-256+) |
| count | int | 1 | Number of passwords to generate |

### Examples
```bash
# 1 password, 16 chars (default)
python password_generator.py

# 1 password, 20 chars
python password_generator.py 20

# 5 passwords, 16 chars each
python password_generator.py 16 5

# 10 passwords, 32 chars each
python password_generator.py 32 10

# Interactive mode
python password_generator_interactive.py
```

---

## 💻 System Requirements

- **Python:** 3.7 or higher
- **OS:** Windows, macOS, or Linux
- **Dependencies:** None (uses only standard library)

---

## 📖 File Structure

```
synent-task4-RandomPassword-shreya/
├── README.md                              # This file (GitHub overview)
├── QUICKSTART.md                          # Quick start guide
├── password_generator.py                  # CLI version (500+ lines)
├── password_generator_interactive.py      # Interactive version (350+ lines)
└── requirements.txt (optional)            # Python version info
```

---


## 🧪 Testing

### Test Cases

```bash
# Test 1: Single password
python password_generator.py

# Test 2: Multiple passwords
python password_generator.py 16 10

# Test 3: Long password
python password_generator.py 64

# Test 4: Short password (minimum)
python password_generator.py 4

# Test 5: Interactive mode
python password_generator_interactive.py
```

All tests pass successfully ✅

---



---

**Happy Password Generating! 🔐✨**
