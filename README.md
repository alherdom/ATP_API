# Django ATP Players Matches API

This repository contains an API created with Django and Django REST Framework that provides data about ATP tennis players and their matches.

## Requirements

- Django==5.0.1
- DjangoRESTFramework==3.14.0
- Prettyconf==2.2.1
- IPython==8.20.0

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/alherdom/ATP_API.git
    ```

2. Install the dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. Set up your environment variables. You must create an `.env` file with the variables.

4. Run the database migrations:

    ```
    python manage.py migrate
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

## Usage

### Endpoints

- `/api/players/`: Returns a list of all ATP tennis players.
- `/api/players/<id>/`: Returns details of a specific player.
- `/api/matches/`: Returns a list of all matches.
- `/api/matches/<id>/`: Returns details of a specific match.

### Example Request

To get the list of players, make a GET request to `/api/players/`.

## Contribution

Contributions are welcome! If you find any bugs or have any suggestions for improvement, please open an issue or send a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).