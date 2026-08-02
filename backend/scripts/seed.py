"""Seed script to generate realistic mock expense data."""
import random
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Add backend root to path so imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from src.storage.json_file_manager import JsonFileManager
from src.models.expense import Expense
from src.core.config import get_settings
from src.core.constants import DEFAULT_CATEGORIES

# Realistic expense titles by category
EXPENSE_TEMPLATES = {
    "Food & Dining": [("Morning Coffee", 3, 7), ("Lunch", 8, 18), ("Groceries", 30, 120), ("Dinner Out", 20, 80), ("Fast Food", 6, 15), ("Pizza Delivery", 12, 30)],
    "Transportation": [("Gas", 25, 60), ("Uber Ride", 8, 35), ("Bus Pass", 50, 100), ("Parking", 5, 20), ("Car Wash", 10, 30)],
    "Housing": [("Rent", 800, 2000), ("Home Repair", 50, 300), ("Furniture", 100, 500)],
    "Utilities": [("Electric Bill", 50, 150), ("Water Bill", 20, 60), ("Internet", 40, 80), ("Phone Bill", 30, 90)],
    "Healthcare": [("Doctor Visit", 50, 200), ("Pharmacy", 10, 80), ("Gym Membership", 25, 60)],
    "Entertainment": [("Movie Tickets", 10, 30), ("Netflix", 10, 20), ("Concert Tickets", 30, 150), ("Video Games", 20, 70)],
    "Shopping": [("Clothing", 20, 150), ("Electronics", 30, 500), ("Amazon Order", 15, 200), ("Shoes", 40, 180)],
    "Education": [("Online Course", 10, 200), ("Books", 10, 40), ("School Supplies", 15, 50)],
    "Travel": [("Flight Ticket", 150, 600), ("Hotel", 80, 250), ("Travel Insurance", 30, 80)],
    "Personal Care": [("Haircut", 15, 50), ("Skincare Products", 10, 60)],
    "Insurance": [("Car Insurance", 80, 200), ("Health Insurance", 200, 500)],
    "Savings & Investments": [("Stock Purchase", 50, 500), ("Savings Deposit", 100, 1000)],
    "Gifts & Donations": [("Birthday Gift", 20, 100), ("Charity Donation", 10, 200)],
    "Other": [("Miscellaneous", 5, 50), ("Subscription", 5, 30)],
}

def generate_expenses(count: int = 75) -> list[Expense]:
    expenses = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)  # 6 months of data
    
    for _ in range(count):
        category = random.choice(DEFAULT_CATEGORIES)
        templates = EXPENSE_TEMPLATES.get(category, [("Miscellaneous", 5, 50)])
        title, min_amount, max_amount = random.choice(templates)
        amount = round(random.uniform(min_amount, max_amount), 2)
        days_ago = random.randint(0, (end_date - start_date).days)
        expense_date = (end_date - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        
        expenses.append(Expense(
            title=title,
            amount=amount,
            category=category,
            date=expense_date,
        ))
    
    return expenses

def main():
    print("🌱 Seeding expense data...")
    settings = get_settings()
    fm = JsonFileManager(settings.data_file_path)
    fm.ensure_file_exists()
    
    data = fm.read_data()
    expenses = generate_expenses(75)
    data["expenses"] = [e.to_dict() for e in expenses]
    fm.write_data(data)
    
    print(f"✅ Created {len(expenses)} expenses")
    total = sum(e.amount for e in expenses)
    print(f"💰 Total: ${total:,.2f}")
    categories_used = set(e.category for e in expenses)
    print(f"📁 Categories used: {len(categories_used)}")
    print(f"📅 Date range: {min(e.date for e in expenses)} to {max(e.date for e in expenses)}")
    print(f"\n📄 Data saved to: {settings.data_file_path}")

if __name__ == "__main__":
    main()
