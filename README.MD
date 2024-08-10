# SEI SEBPT220 Project 3: SpoiledPotato

SpoiledPotato is an Entertainment Wiki application enabling user to seamlessly review to All Television shows in their area.

## How It Works

SpoiledPotato allows users to browse a database of movies, tv shows, plays, view details for each movie including the cast, and add new movies to the database. Users can also search for actors and see the movies they've been in.

## Live Demo

![Application Page](/assets/img/image.png)

[Live Demo Site]()

## Features

### Movie Management

- **Add New Movies:** Users can add new movies to the database, specifying details like title, length, rating, and a list of actors.
- **Edit Movies:** Update movie details including the list of actors associated with the movie.
- **View Movie Details:** See detailed information about each movie, including a list of actors.

### Actor Management

- **Add New Actors:** Users can add actors to the database with details like name, birthday, and bio.
- **Search for Actors:** Search for actors to view their details and the movies they’ve been part of.
- **View Actor Details:** See an actor's biography and the movies they've been in.

## User Stories

1. **Create an account:**
   - As a user, I want to create an account to save my reviews and preferences.
2. **Add a new movie:**
   - As a user, I want to add new movies to the database to keep the collection up-to-date.
3. **Search for an actor:**
   - As a user, I want to search for an actor to see their biography and list of movies.
4. **View movie details:**
   - As a user, I want to view the details of a movie to learn more about it.

## Setup Instructions for Local Deployment

To set up this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tflinch/SpoiledPotato.git
   ```

2. **Navigate to the project directory:**

   ```bash
    cd spoiledpotato
   ```

3. **Install dependencies:**

   ``` bash
    pip install -r requirements.txt
   ```

4. **Set up the environment variables:**

   - Create a `.env` file in the root directory.
   - Add the following environment variables:
   
    ``` bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=your_database_url
    ```

5. **Run the application:**

   ``` bash
   python manage.py runserver
   ```

6. **Open your browser and visit:**
   ```
   http://localhost:8000
   ```

## Code Snippets

### Search Form
- This form allows users to query the database.
    ```python
    class SearchForm(forms.Form):
        query = forms.CharField(label='Search',max_length=100)
    ```
    ```html
    <form method="GET" action="{% url 'search_view' %}" class="navbar-search">
      <input type="text" name="query" placeholder="Search..." value="{{ request.GET.query }}" class="search-input">
    </form>
    ```

### Home_Page Recent Movies
- Querys the database for most recently added movies
    ```python
    def home_page(request):
    recent_movies = Movie.objects.order_by('-id')[:5]
    return render(request, 'spoiledpotato/home_page.html', {'recent_movies': recent_movies})
    ```


## Inspiration

- [RottenTomatoes](https://www.rottentomatoes.com/)

## Mockups

![SpoiledPotato](assets/img/FrontendMockup.png)
![SpoiledPotato_p2](assets/img/FrontendMockup_p2.png)
![Backend MockuP](assets/img/BackendMockup.png)
![ERD](assets/img/ERD.png)

