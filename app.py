from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__)

#TODO: change this get randomly from jsonplaceholder
tasks = [
    {
        'id': 1,
        'name': 'Write SQL',
        'checked': False
    },
    {
        'id': 2,
        'name': 'Write Python',
        'checked': True
    }
]

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if (request.method == "POST"):
        task_name = request.form["task_name"]
        cur_id = random.randint(1, 1000)
        tasks.append(
            {
            'id': cur_id,
            'name': task_name,
            'checked': False
            }
        )
        return redirect(url_for("home"))
    return render_template("index.html", items=tasks)

# def getRandomTask():
    
#     random_id = random.randint(1,100)
#     api_url = f"https://jsonplaceholder.typicode.com/todos/{random_id}"
#     tasks.append(
#         {
#             'id': cur_id,
#             'name': task_name,
#             'checked': False
#             }
#     )

@app.route("/checked/<int:task_id>", methods=["POST"])
def checked_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['checked'] = not task['checked']  # Toggle the status
            break
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
    return redirect(url_for("home"))

# Below is needed because by default Flask binds to local host, which prevents external access from Docker
# This allows flask to listen on all available network interfaces, including Docker
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)