def assign_theme(text):
    text = text.lower()
    if any(word in text for word in ['login', 'access', 'password', 'account locked']):
        return 'Account Access Issues'
    elif any(word in text for word in ['transfer', 'transaction', 'delay', 'pending', 'fail']):
        return 'Transaction Performance'
    elif any(word in text for word in ['interface', 'design', 'easy', 'navigation', 'ui']):
        return 'User Interface & Experience'
    elif any(word in text for word in ['support', 'help', 'customer service', 'response']):
        return 'Customer Support'
    elif any(word in text for word in ['feature', 'add', 'request', 'option']):
        return 'Feature Requests'
    else:
        return 'Other'