# Academic Documentation Center

The **Academic Documentation Center** is a web-based application designed to manage and centralize all documentation for an academic institution. It provides a platform where users can easily store, retrieve, and manage academic documents such as research papers, theses, articles, and reports. The main objective is to create an efficient and organized documentation system that allows faculty, staff, and students to have easy access to important academic materials.

## Key Features
- **User Authentication and Authorization**: Log in to add, update, or delete documents with role-based access control.
- **Document Management**: Upload, categorize, and manage documents, including metadata such as author, department, and publication date.
- **API Access**: RESTful API for integration with other systems and programmatic access to document data.
- **Scalable and Flexible**: Uses MongoDB to handle diverse document types and metadata.

## Technologies Used
- **FastAPI**: A modern, high-performance web framework for building APIs with Python.
- **MongoDB**: A NoSQL database to handle non-relational and flexible data structures.
- **Uvicorn**: ASGI server to run the FastAPI application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JamalXVI/document-center.git
   cd document-center
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for MongoDB:
   ```bash
   export MONGO_URL="mongodb://localhost:27017"
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints
- **POST /users/**: Create a new user.
- **POST /documents/**: Upload a new document.
- **GET /documents/**: Retrieve all documents.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.