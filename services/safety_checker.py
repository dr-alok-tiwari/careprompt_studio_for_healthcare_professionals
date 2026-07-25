import re
from dataclasses import dataclass

@dataclass
class SafetyResult:
    risk: str
    flags: list[str]
    sanitised_text: str

PATTERNS = {
    "Possible email address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Possible phone number": r"(?<!\d)(?:\+?91[-\s]?)?[6-9]\d{9}(?!\d)",
    "Possible Aadhaar-like number": r"(?<!\d)\d{4}[ -]?\d{4}[ -]?\d{4}(?!\d)",
    "Possible medical record identifier": r"\b(?:MRN|UHID|Patient\s*ID|Hospital\s*ID)\s*[:#-]?\s*[A-Z0-9-]{4,}\b",
    "Possible exact address": r"\b(?:house|flat|plot|street|road|lane|sector)\s+(?:no\.?\s*)?[A-Za-z0-9/-]+",
}

HIGH_RISK_WORDS = ["prescribe", "dosage", "dose change", "final diagnosis", "stop medication", "emergency treatment"]

def inspect_text(text: str) -> SafetyResult:
    flags = []
    sanitised = text
    for label, pattern in PATTERNS.items():
        if re.search(pattern, text, flags=re.I):
            flags.append(label)
            sanitised = re.sub(pattern, "[REDACTED]", sanitised, flags=re.I)
    risk = "High" if any(w in text.lower() for w in HIGH_RISK_WORDS) else ("Moderate" if flags else "Low")
    return SafetyResult(risk=risk, flags=flags, sanitised_text=sanitised)
