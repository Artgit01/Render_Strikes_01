from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "System Online: Render_Strikes_01 is active."

if __name__ == "__main__":
    # This part is critical for Render!
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
