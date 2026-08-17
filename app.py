from flask import Flask, render_template

app = Flask(__name__)

# Replace the placeholders below with your actual details
STUDENT_NAME = "[MY NAME]"
STUDENT_ID = "[MY STUDENT ID]"
COURSE_NAME = "[MY COURSE NAME]"


@app.route("/")
def index():
    return render_template(
        "index.html",
        name=STUDENT_NAME,
        student_id=STUDENT_ID,
        course=COURSE_NAME,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
