

---

# SQL Query Generator Web App

Welcome to the **SQL Query Generator Web App**! This web application uses **Google Gemini's Generative AI Model** to generate SQL queries based on natural language prompts. The app leverages the power of generative AI to simplify SQL query creation, allowing users to convert plain English requests into SQL code seamlessly.

---

## Features

- **Generative AI Integration:** Utilizes Google Gemini's powerful generative AI model.
- **SQL Query Generation:** Transforms natural language input into accurate SQL queries.
- **User-Friendly Interface:** Built with Streamlit for an easy-to-use web interface.
- **Table Visualization:** Displays input and output tables along with the generated SQL query for better understanding.

---

## Prerequisites

Before running the app, ensure that you have the following prerequisites:

- Python 3.7 or higher
- **Google API Key**: You will need to obtain an API key from **Google AI Studio** to access the generative AI model.

---

## Installation Steps

Follow these steps to set up the project locally:

### 1. Clone the Repository or Download the ZIP File

You can either clone the repository using Git or download it as a ZIP file:

- **Option 1: Clone the Repository**

    ```bash
    git clone https://github.com/Hamza-Meer007/sql-query-generator.git
    ```

- **Option 2: Download the ZIP File**

    Alternatively, you can download the repository as a ZIP file from [here](https://github.com/Hamza-Meer007/sql-query-generator).

### 2. Install Required Dependencies

After cloning or extracting the ZIP file, open your terminal, navigate to the project directory, and install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

### 3. Obtain Your Google API Key

In order to use the **Generative AI Model** from **Google Gemini**, you need to get an API key from **Google AI Studio**.

#### Steps to Get the API Key:

1. Go to the [Google AI Studio](https://cloud.google.com/ai).
2. Create a project or select an existing project.
3. Enable the **Gemini API** under the API & Services section.
4. Go to the **Credentials** page and generate a new API key.
5. Once the key is generated, copy it.

### 4. Set Up the API Key

Create a `.env` file in the root directory of the project and add your API key as follows:

```bash
GOOGLE_API_KEY=your_generated_api_key_here
```

### 5. Running the App

Once you have installed the dependencies and set up the API key, follow these steps to run the app:

1. Open your terminal and navigate to the project directory.
2. Run the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

3. After the app starts, open your web browser and visit the URL provided by Streamlit (usually `http://localhost:8501`).
4. You can now start entering natural language prompts, and the app will generate SQL queries for you!

---

## Example Use Case

**Input:**

- **Prompt:** Show me the customers whose age is between 30 and 40 from the 'Customers' table.

**Output:**

The app will generate the following SQL query:

```sql
SELECT * FROM Customers WHERE age BETWEEN 30 AND 40;
```

**Input Table:**

| CustomerID | Name       | Age | Address             |
|------------|------------|-----|---------------------|
| 1          | John Doe   | 35  | 123 Main Street     |
| 2          | Jane Smith | 28  | 456 Elm Street      |
| 3          | Bill Jones | 40  | 789 Oak Street      |
| 4          | Mary Brown | 33  | 1011 Willow Street  |

**Output Table:**

| CustomerID | Name       | Age | Address             |
|------------|------------|-----|---------------------|
| 1          | John Doe   | 35  | 123 Main Street     |
| 3          | Bill Jones | 40  | 789 Oak Street      |
| 4          | Mary Brown | 33  | 1011 Willow Street  |

---

## Contributing

We welcome contributions to this project! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

### How to Contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request with a description of your changes.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it.

---

## Contact

For any inquiries or questions, feel free to reach out to the project maintainer:

**Hamza Meer**  
[LinkedIn Profile](https://www.linkedin.com/in/hamza-meer)  
[GitHub Profile](https://github.com/Hamza-Meer007/)

---

