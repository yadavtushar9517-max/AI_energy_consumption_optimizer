def generate_recommendation(prediction, temperature, occupancy):

    recommendations = []

    if prediction > 5:
        recommendations.append("Turn off unused electrical appliances.")

    if temperature > 30:
        recommendations.append("Use fans before switching on AC.")

    if occupancy <= 1:
        recommendations.append("Reduce lighting in unused rooms.")

    if prediction < 3:
        recommendations.append("Excellent! Your energy consumption is efficient.")

    return recommendations