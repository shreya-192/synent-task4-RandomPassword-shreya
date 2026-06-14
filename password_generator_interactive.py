#!/usr/bin/env python3
"""
Interactive Password Generator - Generate secure passwords with prompts

This version provides an interactive menu for generating passwords with
various options and customization.

Usage:
    python password_generator_interactive.py
"""

import random
import string
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
        
        # Fill remaining length with random characters
        remaining_length = length - 4
        password_chars.extend(
            random.choice(self.all_chars) for _ in range(remaining_length)
        )
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def check_strength(self, password: str) -> str:
        """
        Analyze password strength.
        
        Args:
            password (str): Password to analyze
        
        Returns:
            str: Strength level description
        """
        has_upper = any(c in self.uppercase for c in password)
        has_lower = any(c in self.lowercase for c in password)
        has_digit = any(c in self.digits for c in password)
        has_special = any(c in self.special for c in password)
        length = len(password)
        
        score = sum([has_upper, has_lower, has_digit, has_special])
        
        if length >= 16 and score == 4:
            return "Very Strong 💪"
        elif length >= 12 and score >= 3:
            return "Strong 🔒"
        elif length >= 8 and score >= 3:
            return "Good ✓"
        else:
            return "Fair ⚠️"


def print_menu():
    """Display interactive menu."""
    print("\n" + "="*50)
    print("🔐 PASSWORD GENERATOR - INTERACTIVE MODE")
    print("="*50)
    print("1. Generate single password (default: 16 chars)")
    print("2. Generate multiple passwords")
    print("3. Generate with custom length")
    print("4. Generate with custom settings")
    print("5. Exit")
    print("="*50)


def get_positive_int(prompt: str, default: int = None) -> int:
    """Get positive integer input from user."""
    while True:
        try:
            value = input(prompt).strip()
            if not value and default:
                return default
            value = int(value)
            if value < 1:
                print("❌ Please enter a positive number")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number")


def interactive_mode():
    """Run interactive password generation mode."""
    generator = PasswordGenerator()
    
    while True:
        print_menu()
        choice = input("Select option (1-5): ").strip()
        
        if choice == '1':
            # Single default password
            password = generator.generate(16)
            strength = generator.check_strength(password)
            print(f"\n✅ Generated Password:")
            print(f"   {password}")
            print(f"   Strength: {strength}")
            print(f"   Length: 16 characters")
        
        elif choice == '2':
            # Multiple passwords
            count = get_positive_int("\nHow many passwords? (default: 3): ", 3)
            length = get_positive_int("Password length? (default: 16): ", 16)
            
            if length < 4:
                print("❌ Length must be at least 4")
                continue
            
            print(f"\n✅ Generating {count} password(s):\n")
            for i in range(count):
                password = generator.generate(length)
                strength = generator.check_strength(password)
                print(f"{i+1}. {password} [{strength}]")
        
        elif choice == '3':
            # Custom length
            length = get_positive_int("\nEnter desired password length (min: 4): ", 16)
            
            if length < 4:
                print("❌ Length must be at least 4")
                continue
            
            password = generator.generate(length)
            strength = generator.check_strength(password)
            print(f"\n✅ Generated Password ({length} chars):")
            print(f"   {password}")
            print(f"   Strength: {strength}")
        
        elif choice == '4':
            # Custom settings
            length = get_positive_int("\nEnter password length (min: 4): ", 16)
            count = get_positive_int("How many passwords? (default: 1): ", 1)
            
            if length < 4:
                print("❌ Length must be at least 4")
                continue
            
            print(f"\n✅ Generated Passwords:\n")
            for i in range(count):
                password = generator.generate(length)
                strength = generator.check_strength(password)
                print(f"{i+1}. {password} [{strength}]")
        
        elif choice == '5':
            print("\n👋 Thanks for using Password Generator!")
            print("🔒 Stay secure! Remember to use unique passwords.\n")
            break
        
        else:
            print("❌ Invalid option. Please select 1-5")


def main():
    """Main entry point."""
    print("\n" + "🔐"*25)
    print("WELCOME TO PASSWORD GENERATOR")
    print("🔐"*25 + "\n")
    
    interactive_mode()


if __name__ == "__main__":
    main()
