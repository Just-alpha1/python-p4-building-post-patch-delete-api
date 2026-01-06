#!/usr/bin/env python3
"""
Test script to verify the API functionality
Run this after starting the Flask server
"""

import requests
import json

BASE_URL = "http://localhost:5556"

def test_get_reviews():
    """Test GET /reviews"""
    print("Testing GET /reviews...")
    try:
        response = requests.get(f"{BASE_URL}/reviews")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

def test_get_review_by_id():
    """Test GET /reviews/<id>"""
    print("Testing GET /reviews/1...")
    try:
        response = requests.get(f"{BASE_URL}/reviews/1")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

def test_post_review():
    """Test POST /reviews"""
    print("Testing POST /reviews...")
    try:
        data = {
            "score": 8,
            "comment": "Great game!",
            "game_id": 1,
            "user_id": 1
        }
        response = requests.post(f"{BASE_URL}/reviews", json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

def test_patch_review():
    """Test PATCH /reviews/<id>"""
    print("Testing PATCH /reviews/1...")
    try:
        data = {
            "score": 9,
            "comment": "Updated review - even better!"
        }
        response = requests.patch(f"{BASE_URL}/reviews/1", data=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

def test_delete_review():
    """Test DELETE /reviews/<id>"""
    print("Testing DELETE /reviews/1...")
    try:
        response = requests.delete(f"{BASE_URL}/reviews/1")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 50)

if __name__ == "__main__":
    print("API Test Script")
    print("Make sure the Flask server is running on port 5555")
    print("=" * 50)
    
    test_get_reviews()
    test_get_review_by_id()
    test_post_review()
    test_patch_review()
    test_delete_review()
    
    print("All tests completed!")
