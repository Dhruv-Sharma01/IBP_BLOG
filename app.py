from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database setup
DB_NAME = "blog.db"

def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Create the table on startup
create_table()

@app.route('/')
def index():
    # Display all blog posts
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    # Create a new blog post
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        connection.commit()
        connection.close()

        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    # Edit an existing blog post
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        cursor.execute("UPDATE posts SET title=?, content=? WHERE id=?", (title, content, post_id))
        connection.commit()
        connection.close()

        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM posts WHERE id=?", (post_id,))
    post = cursor.fetchone()
    connection.close()

    return render_template('edit.html', post=post)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Delete a blog post
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE id=?", (post_id,))
    connection.commit()
    connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
