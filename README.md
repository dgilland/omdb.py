# omdb.py

Python wrapper around `The Open Movie Database API` (a.k.a. `OMDb API`): http://omdbapi.com/

Version: `0.0.1`

**NOTE:** This library and its author are not endorsed by or affiliated with [OMDbAPI.com](http://omdbapi.com/).

## Installation

Using `pip`:

```bash
pip install omdb
```

### Dependencies

- `requests>=2.0.1`

## API

Each `omdb.py` method supports the same parameters as the `OMDb API`.

### Paramters

| omdb.py Param | OMDb API Param | Value | Description |
| --- | --- | --- | --- |
| `search` | `s` | string **(optional)** | title of media to search for |
| `imdbid` | `i` | string **(optional)** | a valid IMDb ID |
| `title` | `t` | string **(optional)** | title of media to return |
| `year` | `y` | year **(optional)** | year of media |
| `fullplot=True` | `plot=full` | `full` | include extended plot |
| `fullplot=False` | `plot=short` | `short` | include short plot **(default)** |
| `tomatoes=True` | `tomatoes=true` | `true` **(optional)** | add Rotten Tomatoes data to response |

**NOTE:** By default all `OMDb API` responses are formatted as `JSON`. However, `OMDb API` also supports responses formatted as `XML`. Since `omdb.py` will handle `JSON` to `dict` conversion automatically, it's generally not necessary (nor is it supported by the main `ombd.py` methods) to return `XML` formatted responses. But this can be accomplished by directly using `omdb.Client`:

```python
from omdb import Client

# must use OMDb API parameters
res = Client.request(t='True Grit', y=1969, r='xml')
xml_content = res.content
```

### Methods

All methods are accessible via:

```python
import omdb

omdb.<method>
```

| Method | Description | Returns |
| --- | --- | --- |
| `get(**params)` | Generic request to OMDb API (requires keyword argument passing of all parameters). | `dict` |
| `search(search, **params)` | Search by string. | `dict` |
| `imdbid(imdbid, **params)` | Get by IMDB ID | `dict` |
| `title(title, **params)` | Get by title | `dict` |

### Client

While generally not necessary, one can use the lower level `OMDb API Client` for accessing the API:

```python
from omdb import Client
```

| Class Methods | Description |
| --- | --- |
| `get(**omdb_params)` | Generic request to OMDb API which can be used for any type of query. Returns `dict`. |
| `request(**omdbapi_params)` | Lower-level request to OMDb API which accepts URL query parameters supported by OMDb API. Returns `request.Response`. |

## Usage

### General Import

```python
import omdb
```

### omdb.get()

```python
# include full plot and Rotten Tomatoes data
omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)
```

**Returns:**

```json
{
  "Plot":"The murder of her father sends a teenage tomboy, Mattie Ross, (Kim Darby), on a mission of 'justice', which involves avenging her father's death. She recruits a tough old marshal, 'Rooster' Cogburn (John Wayne), because he has 'grit', and a reputation of getting the job done. The two are joined by a Texas Ranger, La Boeuf, (Glen Campbell), who is looking for the same man (Jeff Corey) for a separate murder in Texas. Their odyssey takes them from Fort Smith, Arkansas, deep into the Indian Territory (present day Oklahoma) to find their man.",
  "Rated":"G",
  "tomatoImage":"certified",
  "Title":"True Grit",
  "DVD":"21 Mar 2000",
  "tomatoMeter":"90",
  "Writer":"Charles Portis, Marguerite Roberts",
  "tomatoUserRating":"3.8",
  "Production":"Paramount Home Video",
  "Actors":"John Wayne, Kim Darby, Glen Campbell, Jeremy Slate",
  "tomatoFresh":"43",
  "Type":"movie",
  "imdbVotes":"25,215",
  "Website":"N/A",
  "Director":"Henry Hathaway",
  "Poster":"http://ia.media-imdb.com/images/M/MV5BMTYwNTE3NDYzOV5BMl5BanBnXkFtZTcwNTU5MzY0MQ@@._V1_SX300.jpg",
  "tomatoRotten":"5",
  "tomatoConsensus":"N/A",
  "Released":"11 Jun 1969",
  "tomatoUserReviews":"24,725",
  "Genre":"Adventure, Western, Drama",
  "tomatoUserMeter":"81",
  "imdbRating":"7.3",
  "BoxOffice":"N/A",
  "Runtime":"2 h 8 min",
  "tomatoReviews":"48",
  "imdbID":"tt0065126",
  "Response":"True",
  "tomatoRating":"7.9",
  "Year":"1969"
}
```

### omdb.search()

```python
# search by string
omdb.search('True Grit')
```

**Returns:**

```json
{
  "Search":[
	{
	  "imdbID":"tt1403865",
	  "Year":"2010",
	  "Type":"movie",
	  "Title":"True Grit"
	},
	{
	  "imdbID":"tt0065126",
	  "Year":"1969",
	  "Type":"movie",
	  "Title":"True Grit"
	},
	{
	  "imdbID":"tt0078422",
	  "Year":"1978",
	  "Type":"movie",
	  "Title":"True Grit"
	},
	{
	  "imdbID":"tt1915447",
	  "Year":"2011",
	  "Type":"episode",
	  "Title":"Old vs. New: True Grit"
	},
	{
	  "imdbID":"tt0732294",
	  "Year":"1989",
	  "Type":"episode",
	  "Title":"True Grit"
	},
	{
	  "imdbID":"tt2644308",
	  "Year":"2012",
	  "Type":"episode",
	  "Title":"True Grit"
	},
	{
	  "imdbID":"tt2192761",
	  "Year":"2011",
	  "Type":"episode",
	  "Title":"True Grit"
	},
	{
	  "imdbID":"tt2135225",
	  "Year":"2010",
	  "Type":"episode",
	  "Title":"Little Fockers/True Grit/Season of the Witch"
	},
	{
	  "imdbID":"tt1454553",
	  "Year":"2007",
	  "Type":"movie",
	  "Title":"South 5: True Grit"
	},
	{
	  "imdbID":"tt0799861",
	  "Year":"2006",
	  "Type":"series",
	  "Title":"CMT: True Grit"
	}
  ]
}
```

### omdb.imdbid()

```python
# get by IMDB id
omdb.imdbid('tt0065126')
```

**Returns:**

```json
{
  "Plot":"A drunken, hard-nosed U.S. Marshal and a Texas Ranger help a stubborn young woman track down her father's murderer in Indian territory.",
  "Rated":"G",
  "Title":"True Grit",
  "Poster":"http://ia.media-imdb.com/images/M/MV5BMTYwNTE3NDYzOV5BMl5BanBnXkFtZTcwNTU5MzY0MQ@@._V1_SX300.jpg",
  "Writer":"Charles Portis, Marguerite Roberts",
  "Response":"True",
  "Director":"Henry Hathaway",
  "Released":"11 Jun 1969",
  "Actors":"John Wayne, Kim Darby, Glen Campbell, Jeremy Slate",
  "Year":"1969",
  "Genre":"Adventure, Western, Drama",
  "Runtime":"2 h 8 min",
  "Type":"movie",
  "imdbRating":"7.3",
  "imdbVotes":"25,215",
  "imdbID":"tt0065126"
}
```

### omdb.title()

```python
# get by title
omdb.title('True Grit')
```

**Returns:**

```json
{
  "Plot":"A tough U.S. Marshal helps a stubborn young woman track down her father's murderer.",
  "Rated":"PG-13",
  "Title":"True Grit",
  "Poster":"http://ia.media-imdb.com/images/M/MV5BMjIxNjAzODQ0N15BMl5BanBnXkFtZTcwODY2MjMyNA@@._V1_SX300.jpg",
  "Writer":"Joel Coen, Ethan Coen",
  "Response":"True",
  "Director":"Ethan Coen, Joel Coen",
  "Released":"22 Dec 2010",
  "Actors":"Jeff Bridges, Matt Damon, Hailee Steinfeld, Josh Brolin",
  "Year":"2010",
  "Genre":"Adventure, Drama, Western",
  "Runtime":"1 h 50 min",
  "Type":"movie",
  "imdbRating":"7.7",
  "imdbVotes":"174,273",
  "imdbID":"tt1403865"
}
```

### omdb.Client.get()

```python
omdb.Client.get()
```

**Returns:**

Same as `omdb.get()`.

### omdb.Client.request()

```python
# lower level API request
omdb.Client.request(t='True Grit', y=1969, plot='full', tomatoes='true')
```

**Returns:**

A `requests.Response` object.

## Errors and Exceptions

Under the hood, `omdb.py` uses the [requests](http://www.python-requests.org/) library. For a listing of explicit exceptions raised by `requests`, see [Errors and Exceptions](http://www.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions).

By default `requests` will not raise an `Exception` when an HTTP response's status code is not `200`. However, `omdb.py` _WILL_ raise an `requests.exceptions.HTTPError` error for any response with a non-`200` status code.

## LICENSE

This software is licensed under the BSD License.

## TODO

- More tests (besides just doctests) in `tests/`.
- Implement data structures to better represent returned data (instead of direct API data pass-through)
- Handle `Error` cases in responses (e.g. return an empty list when no search results found instead of `{"Response":"False","Error":"Movie not found!"}`)

