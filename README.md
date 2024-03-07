**README.md:**

```markdown
# Flask Blog

This is a simple CRUD (Create, Read, Update, Delete) blog application built with Flask and SQLite. It provides basic functionality for managing blog posts, including creating new posts, viewing existing posts, updating posts, and deleting posts.

## Features

- Create new blog posts with a title and content.
- View a list of existing blog posts.
- Edit existing blog posts.
- Delete existing blog posts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dhruv-Sharma01/IBP_BLOG.git
   cd IBP_BLOG
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Project Structure

- **app.py**: Main Flask application file.
- **templates/**: HTML templates for the UI.
- **static/**: CSS file for styling.
- **blog.db**: SQLite database file.

## Usage

1. Visit `http://127.0.0.1:5000/` in your web browser to view existing blog posts.
2. Click on "Create New Post" to add a new blog post.
3. Click on "Edit" to modify an existing blog post.
4. Click on "Delete" to remove an existing blog post.

## Customization

Feel free to customize the application, UI, and styles to fit your specific requirements. You can expand the functionality, improve the design, or integrate additional features as needed.

## Contributing

If you have suggestions or find issues, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
