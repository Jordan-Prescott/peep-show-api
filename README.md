# 👁️ The Dobby Club API

Welcome to the Dobby Club! The ultimate API for UK sitcom Peep Show.

![Everythings Cool in Dobby Club](https://cofuvfbkdyfchroaxcvi.supabase.co/storage/v1/object/public/memes/everythings-cool-in-dobby-club.jpeg)

This API is a RESTful API that provides information about the show, its characters, and its episodes and allows you to search for your favourite quotes and memes!. 

The API is built using Python Fast API, Vercel, and Supabase.

## Table of Contents

- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Usage

The best place to start for using the API is the Swagger documentation built into FastAPI. These docs allow you to interact with the API and see the responses in real-time.

You can find the documentation [here](https://thedobby.club/docs).

## Endpoints
- `/actors` - Get all actors or search for an actor by name.
- `/audio` - Listen to your favourite internal monologue from Mark or Jeramy.
- `/avatar` - Get all avatar images or your favourite character for your new phone wallpaper.
- `/characters` - Get all characters or search by name for your favourite.
- `/episode` - Get all episodes or review your favour episode. (mines the Wedding)
- `/quotes` - Search the entire scripts from every series and episode for your favourite quote. (Everythings cool in dobby club)
- `/locations` - Get the locations where our favourite characters have been in the script. (Super Hans flat)
- `/memes` - Find your favourite meme from the show or indulge in some new ones.
- `/scripts` - If you want to read the entire script for an episode or series this is the endpoint for you.
- `/series` - Get all series or search for a series by name. (Whats your favourite series?)

## Authentication

The API doesnt reqiuire any authentication for GET requests. Only POST, PUT, and DELETE requests require authentication and for access to these endpoints, you will need to provide a valid API key which only contributes will have access to. - If you qualify and would like to contribute please reach out [here](#contact)

## Contributing

*I would love some help on this!* If you want to contribute to the code please follow the below steps for changes to the API. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Database

The database is hosted in Supabase which runs Postgres SQL and access needs to be granted to contributors. If you would like to assist with the database please reach out [here](#contact)

### Memes

I want the database to become a meme goldmine for Peep Show fans. 

If you have any memes you would like to add please reach out to me [here](#contact) and I will MAKE SURE theyre added. 

## License

This project is licensed under the MIT License.

## Contact

If you have any questions, feedback, or you would like to contribute feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/jordan-prescott)
