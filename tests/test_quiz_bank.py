import json
from collections import Counter
from pathlib import Path


QUIZZES = Path(__file__).resolve().parents[1] / "data" / "quizzes.json"


def load_quizzes():
    return json.loads(QUIZZES.read_text(encoding="utf-8"))


def test_quiz_bank_has_exactly_500_unique_questions():
    quizzes = load_quizzes()
    assert len(quizzes) == 500
    assert len({question["id"] for question in quizzes}) == 500
    assert len({question["question"] for question in quizzes}) == 500


def test_every_quiz_has_valid_options_answer_and_explanation():
    required = {
        "id",
        "topic",
        "difficulty",
        "context",
        "question",
        "options",
        "answer",
        "explanation",
    }
    for question in load_quizzes():
        assert required.issubset(question)
        assert len(question["options"]) == 4
        assert len(set(question["options"])) == 4
        assert question["answer"] in question["options"]
        assert len(question["explanation"].strip()) >= 40


def test_quiz_bank_balances_topics_and_varies_answer_position():
    quizzes = load_quizzes()
    topic_counts = Counter(question["topic"] for question in quizzes)
    answer_positions = {
        question["options"].index(question["answer"]) for question in quizzes
    }
    assert len(topic_counts) == 10
    assert set(topic_counts.values()) == {50}
    assert answer_positions == {0, 1, 2, 3}
