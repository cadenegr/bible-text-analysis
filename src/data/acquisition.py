"""
Bible Text Data Acquisition Module

This module provides functions to download and process Bible texts from various sources.
"""

import requests
import json
import pandas as pd
from pathlib import Path
import re
from typing import Dict, List, Optional


class BibleDataAcquisition:
    """Class for acquiring Bible text data from various sources."""

    def __init__(self, data_dir: str = "data/raw"):
        """Initialize with data directory path."""
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def download_project_gutenberg_kjv(self) -> str:
        """
        Download King James Version Bible from Project Gutenberg.

        Returns:
            str: Path to downloaded file
        """
        url = "https://www.gutenberg.org/files/10/10-0.txt"
        response = requests.get(url)

        if response.status_code == 200:
            file_path = self.data_dir / "kjv_bible_gutenberg.txt"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Downloaded KJV Bible to {file_path}")
            return str(file_path)
        else:
            raise Exception(f"Failed to download Bible text: {response.status_code}")

    def download_bible_api_data(self, translation: str = "KJV", books: Optional[List[str]] = None) -> str:
        """
        Download Bible data using Bible API.

        Args:
            translation: Bible translation (KJV, ESV, etc.)
            books: List of book names to download (None for all)

        Returns:
            str: Path to downloaded JSON file
        """
        base_url = "https://bible-api.com"

        # Bible books list
        if books is None:
            books = [
                "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
                "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
                "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
                "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
                "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah",
                "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel",
                "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
                "Zephaniah", "Haggai", "Zechariah", "Malachi",
                "Matthew", "Mark", "Luke", "John", "Acts", "Romans",
                "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
                "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians",
                "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews",
                "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John",
                "Jude", "Revelation"
            ]

        bible_data = []

        for book in books:
            try:
                url = f"{base_url}/{book}?translation={translation}"
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    bible_data.append(data)
                    print(f"Downloaded {book}")
                else:
                    print(f"Failed to download {book}: {response.status_code}")
            except Exception as e:
                print(f"Error downloading {book}: {e}")

        # Save to JSON file
        file_path = self.data_dir / f"bible_{translation.lower()}_api.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(bible_data, f, indent=2, ensure_ascii=False)

        print(f"Saved Bible data to {file_path}")
        return str(file_path)

    def create_sample_dataset(self) -> str:
        """
        Create a sample Bible dataset for quick testing.

        Returns:
            str: Path to sample dataset
        """
        sample_verses = [
            {"book": "Genesis", "chapter": 1, "verse": 1, "text": "In the beginning God created the heaven and the earth."},
            {"book": "Genesis", "chapter": 1, "verse": 2, "text": "And the earth was without form, and void; and darkness was upon the face of the deep."},
            {"book": "John", "chapter": 3, "verse": 16, "text": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."},
            {"book": "Psalms", "chapter": 23, "verse": 1, "text": "The LORD is my shepherd; I shall not want."},
            {"book": "Proverbs", "chapter": 3, "verse": 5, "text": "Trust in the LORD with all thine heart; and lean not unto thine own understanding."},
        ]

        file_path = self.data_dir / "bible_sample.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(sample_verses, f, indent=2, ensure_ascii=False)

        print(f"Created sample dataset: {file_path}")
        return str(file_path)


if __name__ == "__main__":
    # Example usage
    bible_data = BibleDataAcquisition()

    # Create sample dataset for testing
    bible_data.create_sample_dataset()

    print("Bible data acquisition module ready!")
    print("Use the class methods to download Bible texts from various sources.")
