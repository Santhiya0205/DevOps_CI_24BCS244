import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.app import add_achievement, portfolio_summary


def test_add_achievement():
    result = add_achievement(
        "Student1",
        "Python Certification"
    )

    assert result["student"] == "Student1"
    assert result["achievement"] == "Python Certification"


def test_portfolio_summary():
    achievements = [
        add_achievement(
            "Student1",
            "Python Certification"
        ),
        add_achievement(
            "Student1",
            "Hackathon Participation"
        )
    ]

    result = portfolio_summary(achievements)

    assert result["total_achievements"] == 2


def test_another_achievement():
    result = add_achievement(
        "Student2",
        "Web Development Certificate"
    )

    assert result["student"] == "Student2"
    assert result["achievement"] == "Web Development Certificate"