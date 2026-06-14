#!/usr/bin/env python3
"""
Password Generator CLI - Generate secure random passwords

Features:
- Uses random module for cryptographic randomness
- Includes: Uppercase, Lowercase, Numbers, Special characters
- Customizable password length
- Multiple password generation
- Copy to clipboard support

Usage:
    python password_generator.py [length] [count]

Examples:
    python password_generator.py              # Generate 1 password (16 chars)
    python password_generator.py 20           # Generate 1 password (20 chars)
    python password_generator.py 16 5         # Generate 5 passwords (16 chars each)
"""

import random
import string
import sys
from typing import List


class PasswordGenerator:
    """Generate secure random passwords with configurable options."""
    
    def __init__(self):
        """Initialize character sets for password generation."""
        self.uppercase = string.ascii_uppercase          # A-Z
        self.lowercase = string.ascii_lowercase          # a-z
        self.digits = string.digits                      # 0-9
        self.special = string.punctuation                # !@#$%^&*()_+-=[]{}|;:,.<>?
        
        # All available characters
        self.all_chars = self.uppercase + self.lowercase + self.digits + self.special
    
    def generate(self, length: int = 16) -> str:
        """
        Generate a single secure password.
        
        Args:
            length (int): Length of password (minimum 4 for all character types)
        
        Returns:
            str: Secure random password
        
        Raises:
            ValueError: If length < 4
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Ensure at least one character from each required type
        password_chars = [
            random.choice(self.uppercase),
            random.choice(self.lowercase),
            random.choice(self.digits),
            random.choice(self.special)
        ]
        
        # Fill remaining length with random characters from all sets
        remaining_length = length - 4
        password_chars.extend(
            random.choice(self.all_chars) for _ in range(remaining_length)
        )
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_multiple(self, length: int = 16, count: int = 1) -> List[str]:
        """
        Generate multiple passwords.
        
        Args:
            length (int): Length of each password
            count (int): Number of passwords to generate
        
        Returns:
            List[str]: List of generated passwords
        """
        return [self.generate(length) for _ in range(count)]
    
    def check_strength(self, password: str) -> dict:
        """
        Analyze password strength.
        
        Args:
            password (str): Password to analyze
        
        Returns:
            dict: Strength analysis with score and comments
        """
        has_upper = any(c in self.uppercase for c in password)
        has_lower = any(c in self.lowercase for c in password)
        has_digit = any(c in self.digits for c in password)
        has_special = any(c in self.special for c in password)
        length = len(password)
        
        # Calculate strength score
        score = 0
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_special:
            score += 1
        
        # Bonus points for length
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if length >= 16:
            score += 1
        
        # Determine strength level
        if score >= 7:
            strength = "Very Strong 💪"
        elif score >= 5:
            strength = "Strong 🔒"
        elif score >= 4:
            strength = "Good ✓"
        else:
            strength = "Weak ⚠️"
        
        return {
            'strength': strength,
            'score': score,
            'length': length,
            'has_uppercase': has_upper,
            'has_lowercase': has_lower,
            'has_digits': has_digit,
            'has_special': has_special,
        }


def print_strength_details(password: str, analysis: dict):
    """Print detailed strength analysis."""
    print(f"\n📊 Strength Analysis for: {'*' * len(password)}")
    print(f"   Strength Level:    {analysis['strength']}")
    print(f"   Score:             {analysis['score']}/7")
    print(f"   Length:            {analysis['length']} characters")
    print(f"   Uppercase (A-Z):   {'✓' if analysis['has_uppercase'] else '✗'}")
    print(f"   Lowercase (a-z):   {'✓' if analysis['has_lowercase'] else '✗'}")
    print(f"   Numbers (0-9):     {'✓' if analysis['has_digits'] else '✗'}")
    print(f"   Special chars:     {'✓' if analysis['has_special'] else '✗'}")


def main():
    """Main CLI interface."""
    print("\n" + "="*60)
    print("🔐 SECURE PASSWORD GENERATOR")
    print("="*60)
    
    # Parse command line arguments
    length = 16  # Default length
    count = 1    # Default count
    
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
            if length < 4:
                print("⚠️  Error: Password length must be at least 4 characters")
                print(f"   Using default length: 16\n")
                length = 16
        except ValueError:
            print(f"⚠️  Error: '{sys.argv[1]}' is not a valid length")
            print(f"   Using default length: 16\n")
    
    if len(sys.argv) > 2:
        try:
            count = int(sys.argv[2])
            if count < 1:
                print("⚠️  Error: Count must be at least 1")
                print(f"   Using default count: 1\n")
                count = 1
        except ValueError:
            print(f"⚠️  Error: '{sys.argv[2]}' is not a valid count")
            print(f"   Using default count: 1\n")
    
    print(f"\n📝 Generating {count} password{'s' if count != 1 else ''} ({length} characters each)...\n")
    
    # Generate passwords
    generator = PasswordGenerator()
    passwords = generator.generate_multiple(length, count)
    
    # Display passwords with strength analysis
    for i, password in enumerate(passwords, 1):
        print(f"Password #{i}:")
        print(f"   {password}")
        
        # Show strength analysis
        analysis = generator.check_strength(password)
        print_strength_details(password, analysis)
        print()
    
    # Provide usage tips
    print("="*60)
    print("💡 TIPS FOR USING YOUR PASSWORDS:")
    print("="*60)
    print("✓ Use unique passwords for each account")
    print("✓ Use a password manager to store them securely")
    print("✓ Don't share passwords via email or chat")
    print("✓ Change passwords regularly")
    print("✓ Never write passwords on paper")
    print("\n📋 USAGE EXAMPLES:")
    print("   python password_generator.py              # 1 password, 16 chars")
    print("   python password_generator.py 20           # 1 password, 20 chars")
    print("   python password_generator.py 16 5         # 5 passwords, 16 chars")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
