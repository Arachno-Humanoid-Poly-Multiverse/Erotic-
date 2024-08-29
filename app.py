from flask import Flask
from AnonXMusic.__main__ import __main__

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    # Return a block of ASCII art text when the root URL is accessed
    return """
███╗░░░███╗██╗░██████╗░██╗░░░██╗███████╗██╗░░░░░  ░█████╗░██╗██╗░░██╗░█████╗░██████╗░░█████╗░
████╗░████║██║██╔════╝░██║░░░██║██╔════╝██║░░░░░  ██╔══██╗╚█║██║░░██║██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██║██║░░██╗░██║░░░██║█████╗░░██║░░░░░  ██║░░██║░╚╝███████║███████║██████╔╝███████║
██║╚██╔╝██║██║██║░░╚██╗██║░░░██║██╔══╝░░██║░░░░░  ██║░░██║░░░██╔══██║██╔══██║██╔══██╗██╔══██║
██║░╚═╝░██║██║╚██████╔╝╚██████╔╝███████╗███████╗  ╚█████╔╝░░░██║░░██║██║░░██║██║░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚══════╝╚══════╝  ░╚════╝░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝"""

# Run the application
if __name__ == "__main__":
    # Set the host to '0.0.0.0' to make the server publicly available
    # Set the port to 8080
    app.run(host='0.0.0.0', port=8080)
