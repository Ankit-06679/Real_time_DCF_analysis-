def calculate_dcf(latest_fcf, growth_rate, discount_rate, terminal_growth, years=5):
    
    projections = []
    fcf = latest_fcf
    
    # Project FCF
    for year in range(1, years + 1):
        fcf = fcf * (1 + growth_rate)
        projections.append(fcf)
    
    # Discount FCF
    discounted_fcf = []
    for i, f in enumerate(projections):
        discounted = f / ((1 + discount_rate) ** (i + 1))
        discounted_fcf.append(discounted)
    
    # Terminal value
    terminal_value = projections[-1] * (1 + terminal_growth) / (discount_rate - terminal_growth)
    discounted_terminal = terminal_value / ((1 + discount_rate) ** years)
    
    total_value = sum(discounted_fcf) + discounted_terminal
    
    return total_value