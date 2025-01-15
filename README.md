# Dev Assessment - Webhook Receiver

Use this repository to construct the Flask webhook receiver.

---

## Setup

1. **Create a new virtual environment:**

    ```bash
    pip install virtualenv
    ```

2. **Create the virtual environment:**

    ```bash
    virtualenv venv
    ```

3. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate
    ```

4. **Install requirements:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Setup MongoDB:**

    - **In a Docker container:**

        ```bash
        docker run --name mongodb -d -p 27017:27017 mongo
        ```

    - **Using MongoDB Atlas:**
        By going to https://www.mongodb.com

    Create a `.env` file with `MONGO_URI` containing the MongoDB URI.

6. **Run the Flask application:**

    ```bash
    python run.py
    ```

    > **Note:** In production, use Gunicorn.

7. **Endpoint:**

    ```bash
    POST http://127.0.0.1:5000/webhook/receiver
    ```

    To set up the webhook for a GitHub repository, you need a public URL. Use a local tunnel or deploy the app on hosted servers.

    Your public endpoint should be:

    ```bash
    POST <server_url>/webhook/receiver
    ```

---

## Screenshots

### Data in MongoDB Docker Container
![MongoDB Data](/screenshots/mongo_screenshot.png)

### Events API Endpoints JSON
![Events API JSON](/screenshots/events_api_screenshot.png)

### Working Frontend
![Frontend](/screenshots/frontend_screenshot.png)