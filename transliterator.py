"""
Transliteration logic for converting Latin characters to visually similar Cyrillic characters.
"""

import logging

logger = logging.getLogger(__name__)

class Transliterator:
    """Handles Latin to Cyrillic transliteration."""
    
    def __init__(self):
        """Initialize the transliteration table."""
        # Visual correspondence table for Latin to Cyrillic
        self.translit_table = {
            'a': 'а', 'b': 'в', 'c': 'с', 'd': 'ԃ', 'e': 'е', 'f': 'ғ', 'g': 'г', 'h': 'н',
            'i': 'і', 'j': 'ј', 'k': 'к', 'l': 'ӏ', 'm': 'м', 'n': 'п', 'o': 'о', 'p': 'р',
            'q': 'ҩ', 'r': 'г', 's': 'ѕ', 't': 'т', 'u': 'ц', 'v': 'ѵ', 'w': 'ш', 'x': 'х',
            'y': 'у', 'z': 'з'
        }
        
        # Create uppercase mappings
        self.uppercase_table = {k.upper(): v.upper() for k, v in self.translit_table.items()}
        
        # Combine both tables
        self.full_table = {**self.translit_table, **self.uppercase_table}
        
        logger.info("Transliterator initialized with visual correspondence table")
    
    def transliterate(self, text: str) -> str:
        """
        Transliterate Latin text to Cyrillic characters.
        
        Args:
            text (str): Input text with Latin characters
            
        Returns:
            str: Transliterated text with Cyrillic characters
        """
        if not text:
            return ""
        
        result = ""
        
        for char in text:
            # Check if character exists in transliteration table
            if char in self.full_table:
                result += self.full_table[char]
            else:
                # Keep original character (numbers, punctuation, spaces, etc.)
                result += char
        
        return result
    
    def get_mapping_info(self) -> dict:
        """
        Get information about the transliteration mapping.
        
        Returns:
            dict: Information about the mapping
        """
        return {
            'total_mappings': len(self.translit_table),
            'supports_case': True,
            'preserves_non_latin': True,
            'sample_mappings': dict(list(self.translit_table.items())[:5])
        }
