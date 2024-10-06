
# End-to-End Text to SQL LLM

This is a Streamlit-based application that converts natural language questions into SQL queries using Google's Gemini LLM. The application processes user queries to interact with a local SQLite database and retrieve relevant data based on the question asked.

## Features

- Converts English questions into SQL queries.
- Retrieves data from a SQLite database based on the generated SQL.
- Displays the results interactively using Streamlit.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/end-to-end-text-to-sql-llm.git
   ```

2. Navigate to the project directory:

   ```bash
   cd end-to-end-text-to-sql-llm
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate   # For Windows
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your `.env` file with your Google API key. Create a `.env` file in the project root and add:

   ```bash
   GOOGLE_API_KEY=your-google-api-key
   ```

## Running the App

To run the application, use the following command:

```bash
streamlit run app.py
```

The app will open in your browser. You can input a natural language question and retrieve SQL results from the SQLite database.

## Example Queries

1. "Tell me the average marks of students."
2. "How many entries or records are present?"
3. "Show all students studying Data Science."

## Technologies Used

- **Streamlit** - For building the web app interface.
- **Google Generative AI (Gemini LLM)** - For converting text to SQL queries.
- **SQLite** - Local database to store student data.
- **dotenv** - To manage environment variables securely.

## SQLite Database

The app uses a local SQLite database (`student.db`) with a `STUDENT` table containing the following columns:

- `NAME` - The student's name.
- `CLASS` - The class the student is enrolled in.
- `SECTION` - The section of the class.
- `MARKS` - The student's marks.

## License

This project is open source and available under the [MIT License](LICENSE).
