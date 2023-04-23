def handle_response(message) -> str:
    p_message = message.lowercase()

    if p_message == 'hello':
        return "HI"
