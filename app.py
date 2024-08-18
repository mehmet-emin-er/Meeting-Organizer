from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# A list to store our meetings, not with database for this task.
meetings = []

# Render main page
@app.route('/')
def index():
    return render_template('index.html')

# Add a new meeting to the list
@app.route('/add', methods=['POST'])
def add_meeting():
    topic = request.form.get('topic')
    date = request.form.get('date')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    participants = request.form.get('participants')

    # Create a new dic
    meeting = {
        'topic': topic,
        'date': date,
        'start_time': start_time,
        'end_time': end_time,
        'participants': participants
    }

    # Append the meeting to the meetings
    meetings.append(meeting)
    # Redirect to the meetings page for overall information
    return redirect(url_for('list_meetings'))

# Update an existing meeting 
@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_meeting(index):
    if request.method == 'POST':
        topic = request.form.get('topic')
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        participants = request.form.get('participants')

        meetings[index] = {
            'topic': topic,
            'date': date,
            'start_time': start_time,
            'end_time': end_time,
            'participants': participants
        }

        return redirect(url_for('list_meetings'))

    meeting = meetings[index]
    return render_template('update.html', meeting=meeting, index=index)

# Delete a meeting operation
@app.route('/delete/<int:index>')
def delete_meeting(index):
    meetings.pop(index)
    return redirect(url_for('list_meetings'))

# Render the page that lists all the meetings
@app.route('/meetings')
def list_meetings():
    return render_template('list.html', meetings=meetings)

if __name__ == '__main__':
    app.run(debug=True)
