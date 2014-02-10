# omdb.py

Python wrapper around `The Open Movie Database API` (a.k.a. `OMDb API`): http://omdbapi.com/

Version: `0.1.1`

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

| OMDb API Param | omdb.py Param | Value | Description |
| --- | --- | --- | --- |
| `s` | `search` | string **(optional)** | title of media to search for |
| `i` | `imdbid` | string **(optional)** | a valid IMDb ID |
| `t` | `title` | string **(optional)** | title of media to return |
| `y` | `year` | year **(optional)** | year of media |
| `plot=full` | `fullplot=True` | `full` | include extended plot |
| `plot=short` | `fullplot=False` | `short` | include short plot **(default)** |
| `tomatoes=true` | `tomatoes=True` | `true` **(optional)** | add Rotten Tomatoes data to response |

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
| `get(**params)` | Generic request to OMDb API (requires keyword argument passing of all parameters). | `Item` |
| `search(search, **params)` | Search by string. | `Search` |
| `imdbid(imdbid, **params)` | Get by IMDB ID | `Item` |
| `title(title, **params)` | Get by title | `Item` |
| `set_default(key, default)` | Set default request parameter | `None` |

### Client

While generally not necessary, one can use the lower level `OMDb API Client` for accessing the API:

```python
from omdb import Client
```

| Class Methods | Description | Returns |
| --- | --- | --- |
| `get(**omdb_params)` | Generic request to OMDb API which can be used for any type of query | `Search` or `GetItem` |
| `request(**omdbapi_params)` | Lower-level request to OMDb API which accepts URL query parameters supported by OMDb API. | `request.Response` |
| `set_default(key, default)` | Set default request parameter. | `None` |

### Models

Movie data returned from the `OMDb API` is converted to a custom dict subclass which allows both `data['key']` and `data.key` access.

There are two main models:

- `omdb.models.Search` (a list of `Item` instances)
- `omdb.models.Item`

Which can be accessed like the following:

```python
import omdb

movie = omdb.title('True Grit')
movie.title == 'True Grit'
movie['title'] == 'True Grit'

search = omdb.search('True Grit')
search[0].title == 'True Grit'
```

All fields from the `OMDb API` are converted from `CamelCaseFields` to `underscore_fields`:

#### Search Item Fields

| OMDb API Fields | omdb.py Fields |
| --- | --- |
| `Title` | `title` |
| `Year` | `year` |
| `Type` | `type` |
| `imdbID` | `imdb_id` |

#### Get Item Fields (tomatoes=False)

| OMDb API Fields | omdb.py Fields |
| --- | --- |
| `Title` | `title` |
| `Year` | `year` |
| `Type` | `type` |
| `Actors` | `actors` |
| `Director` | `director` |
| `Genre` | `genre` |
| `Plot` | `plot` |
| `Poster` | `poster` |
| `Rated` | `rated` |
| `Released` | `released` |
| `Runtime` | `runtime` |
| `Writer` | `writer` |
| `imdbID` | `imdb_id` |
| `imdbRating` | `imdb_rating` |
| `imdbVotes` | `imdb_votes` |

#### Get Item Fields (tomatoes=True)

| OMDb API Fields | omdb.py Fields |
| --- | --- |
| `Title` | `title` |
| `Year` | `year` |
| `Type` | `type` |
| `Actors` | `actors` |
| `Director` | `director` |
| `Genre` | `genre` |
| `Plot` | `plot` |
| `Poster` | `poster` |
| `Rated` | `rated` |
| `Released` | `released` |
| `Runtime` | `runtime` |
| `Writer` | `writer` |
| `imdbID` | `imdb_id` |
| `imdbRating` | `imdb_rating` |
| `imdbVotes` | `imdb_votes` |
| `BoxOffice` | `box_office` |
| `DVD` | `dvd` |
| `Production` | `production` |
| `Website` | `website` |
| `tomatoConsensus` | `tomato_consensus` |
| `tomatoFresh` | `tomato_fresh` |
| `tomatoImage` | `tomato_image` |
| `tomatoMeter` | `tomato_meter` |
| `tomatoRating` | `tomato_rating` |
| `tomatoReviews` | `tomato_reviews` |
| `tomatoRotten` | `tomato_rotten` |
| `tomatoUserMeter` | `tomato_user_meter` |
| `tomatoUserRating` | `tomato_user_rating` |
| `tomatoUserReviews` | `tomato_user_reviews` |

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

### omdb.search()

```python
# search by string
omdb.search('True Grit')
```

### omdb.imdbid()

```python
# get by IMDB id
omdb.imdbid('tt0065126')
```

### omdb.title()

```python
# get by title
omdb.title('True Grit')
```

### omdb.set_default()

```python
# include tomatoes data by default
omdb.set_default('tomatoes', True)
omdb.title('True Grit') == omdb.title('True Grit', tomatoes=True)
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
