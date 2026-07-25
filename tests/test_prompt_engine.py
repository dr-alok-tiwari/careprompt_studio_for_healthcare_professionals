from services.prompt_engine import PromptInputs, build_craft_med, evaluate_prompt

def test_build_prompt_contains_safeguards():
    p=build_craft_med(PromptInputs("fictional","clinician","patient","table","explain","do not diagnose","verify sources","plain language"))
    assert "Do not fabricate" in p and "human-review" in p

def test_score_has_ten_dimensions():
    assert len(evaluate_prompt("task context audience format evidence safety privacy uncertainty verify checklist")) == 10
