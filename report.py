def health_report(probability):

    if probability < 0.30:

        risk = "LOW"

        recommendation = """
Continue a balanced diet.

Exercise at least 30 minutes daily.

Maintain healthy weight.

Annual diabetes screening.
"""

    elif probability < 0.70:

        risk = "MEDIUM"

        recommendation = """
Reduce sugar intake.

Walk every day.

Monitor blood glucose.

Consult a physician.
"""

    else:

        risk = "HIGH"

        recommendation = """
Consult a diabetologist immediately.

Follow a diabetic diet.

Avoid sugary foods.

Regular blood sugar monitoring.

Exercise regularly.
"""

    return risk, recommendation