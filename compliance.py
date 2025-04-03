from datetime import datetime
import re

class ContentGuard:
    def __init__(self):
        self.pii_patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        }
    
    def clean_content(self, text: str) -> str:
        """Basic PII removal without external dependencies"""
        cleaned = text
        for pii_type, pattern in self.pii_patterns.items():
            cleaned = re.sub(pattern, '[REDACTED]', cleaned)
        return cleaned
    
    def check_quality(self, text: str) -> float:
        """Simple content quality check (0-1 scale)"""
        word_count = len(text.split())
        freshness = 1.0 if (datetime.now().year - 2025) <= 1 else 0.5
        return min(word_count * 0.001 + freshness, 1.0)
