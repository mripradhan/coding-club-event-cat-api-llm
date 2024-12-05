# Cat Knock-Knock Jokes API
A fun way to explore and teach APIs to juniors via the WIE x Coding Club event held in Dec 2024.

---

## Features

- **Get All Jokes**: Retrieve a list of all jokes in the collection.
- **Get a Single Joke**: Fetch a joke by its unique ID.
- **Add a Joke**: Contribute your own cat-themed knock-knock joke.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mripradhan/coding-club-event-cat-api-llm
   cd <repository>
   ```

2. Install the required Python packages:
   ```bash
   pip install Flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the API at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. **Home**
   - **URL**: `/`
   - **Method**: `GET`
   - **Description**: Displays a welcome message for the API.

---

### 2. **Get All Jokes**
   - **URL**: `/jokes`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all jokes.
   - **Response**: JSON array of jokes.

---

### 3. **Get a Single Joke**
   - **URL**: `/jokes/<joke_id>`
   - **Method**: `GET`
   - **Description**: Fetches a joke by its ID.
   - **Response**:
     - **Success**: Returns the joke in JSON format.
     - **Error**: Returns a `404` error if the joke is not found.

---

### 4. **Add a Joke**
   - **URL**: `/jokes`
   - **Method**: `POST`
   - **Description**: Adds a new joke to the collection.
   - **Request Body**:
     ```json
     {
       "setup": "string",
       "punchline": "string"
     }
     ```
   - **Response**:
     - **Success**: Returns the newly added joke with its ID.
     - **Error**: Returns a `400` error if the required fields are missing.

---

## Example Requests

### Get All Jokes
```bash
curl http://127.0.0.1:5000/jokes
```

### Get a Single Joke
```bash
curl http://127.0.0.1:5000/jokes/1
```

### Add a Joke
```bash
curl -X POST http://127.0.0.1:5000/jokes \
-H "Content-Type: application/json" \
-d '{"setup": "Knock, knock.", "punchline": "Who’s there? Meow. Meow you doin'?"}'
```

---

## Dependencies

- Python 3.x
- Flask

---

## Notes

- Ensure you have Python and Flask installed before running the app.
- The app runs in debug mode by default. Disable it in production.

---

## License

This project is licensed under the MIT License. Feel free to use and contribute!
