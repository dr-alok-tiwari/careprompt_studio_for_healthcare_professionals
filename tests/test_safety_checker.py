from services.safety_checker import inspect_text

def test_redacts_email():
    r=inspect_text("Contact a@example.com")
    assert "Possible email address" in r.flags and "[REDACTED]" in r.sanitised_text

def test_high_risk_words():
    assert inspect_text("provide a final diagnosis").risk == "High"
