# 👁️ The Dobby Club API

Welcome to the Dobby Club! The ultimate API for UK sitcom Peep Show.

![Everythings Cool in Dobby Club](./assets/cool_in_dobby_club.jpeg)

This API is a RESTful API that provides information about the show, its characters, and its episodes. The API is built using Python Fast API, Vercel, and Supabase.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To install and run the Dobby Club API locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dobby-club-api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd dobby-club-api
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the API:
    ```sh
    uvicorn main:app --reload
    ```

## Usage

To start using the API, you can make requests to the endpoints. Here are some examples:

- Get a list of characters:
    ```sh
    GET /characters
    ```
- Get information about a specific episode:
    ```sh
    GET /episodes/{episode_id}
    ```

## Endpoints

### Get Characters
- **URL:** `/characters`
- **Method:** `GET`
- **Description:** Retrieves a list of legendary character profiles.

### Get Episodes
- **URL:** `/episodes`
- **Method:** `GET`
- **Description:** Retrieves a list of episodes.

### Get Quotes
- **URL:** `/quotes`
- **Method:** `GET`
- **Description:** Retrieves a list of hilarious quotes.

## Authentication

The API doesnt reqiuire any authentication for GET requests. Only POST, PUT, and DELETE requests require authentication and for access to these endpoints, you will need to provide a valid API key which only contributes will have access to.

## Contributing

I would love some help on this! If you want to contribute please follow the below steps for changes to the API. If you would like to assist further with the database please reach out [here](#contact)

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

If you have any questions, feedback, or you would like to contribute feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/jordan-prescott).
