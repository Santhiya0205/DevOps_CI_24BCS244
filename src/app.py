def add_achievement(student, achievement):
    return {
        "student": student,
        "achievement": achievement
    }


def portfolio_summary(achievements):
    return {
        "total_achievements": len(achievements)
    }


if __name__ == "__main__":
    achievements = []

    achievements.append(
        add_achievement(
            "Student1",
            "Python Certification"
        )
    )

    achievements.append(
        add_achievement(
            "Student1",
            "Hackathon Participation"
        )
    )

    print("Student Achievement and Portfolio Management System")
    print(portfolio_summary(achievements))