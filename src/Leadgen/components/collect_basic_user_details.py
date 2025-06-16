import os
import urllib.request as request
from Leadgen import logger
from Leadgen.entity.config_entity import BasicuserConfig

class BasicuserConfiguration:
    def __init__(self, config: BasicuserConfig):
        self.config = config

    def collect_user_details():
        print("=== Basic User Details Collection ===")
        print("Please answer the following questions to help us create your Ideal Customer Profile:\n")
        
        user_data = {}
        
        # Question 1: Business Information
        print("1. What is your business/company name and what industry are you in?")
        user_data['business_info'] = input("   Answer: ").strip()
        
        # Question 2: Products/Services
        print("\n2. What products or services do you offer? (Brief description)")
        user_data['products_services'] = input("   Answer: ").strip()
        
        # Question 3: Current Target Market
        print("\n3. Who do you currently sell to? (Describe your current customers)")
        user_data['current_customers'] = input("   Answer: ").strip()
        
        # Question 4: Business Goals
        print("\n4. What are your main business goals or challenges you're trying to solve?")
        user_data['business_goals'] = input("   Answer: ").strip()
        
        # Question 5: Market Size/Revenue
        print("\n5. What's your approximate annual revenue range or business size?")
        print("   (e.g., Startup, Small (<$1M), Medium ($1M-$10M), Large (>$10M))")
        user_data['business_size'] = input("   Answer: ").strip()
        
        return user_data