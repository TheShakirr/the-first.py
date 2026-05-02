def send_message(name, message = "Welcome!"):
    print(name + "recieves: " + message)

# WARNING: using mtable defaults (like[] or{}) can cause shared data accrosss calls and un expected bugs..

send_message("shakir ")

send_message("shakir ", "congrats, you're learning python!")

