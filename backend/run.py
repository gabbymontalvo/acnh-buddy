from flask import Flask

app = Flask(__name__)

# Fossils API Route TEST
@app.route("/fossils")
def fossils():
    return {"fossils": ["Fossil1", "Fossil2", "Fossil3"]}
    
if __name__ == "__main__":
    app.run(debug=True)