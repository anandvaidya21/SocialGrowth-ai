def generate_strategy(data, keywords):
    strategy = []

    if data.followers < 1000:
        strategy.append("Focus on consistency and daily posting.")

    if "low engagement" in data.problem.lower():
        strategy.append("Use reels and trending audio.")

    if data.engagement < 2:
        strategy.append("Improve hooks in first 3 seconds.")

    if "instagram" in data.niche.lower():
        strategy.append("Post at 6-9 PM for better reach.")

    return strategy