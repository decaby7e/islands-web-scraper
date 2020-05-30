
# Islands Web Scraper

[See the site](https://islands.smp.uq.edu.au)

## Installation

First, install the system requirements:

```bash
$ apt install firefox-geckodriver
```

Then, install the Python requirements:

```bash
$ pip3 install -r requirements.txt
```

## Usage

First, create a file in the root of the repository called `secrets.json` w/ the following structure:

```json
{
  "username": "USERNAME_HERE",
  "password": "PASSWORD_HERE"
}
```

Then, edit the `settings.py` file so that it fits your criteria

Finally, run the program!

```bash
$ python3 main.py
```

## To Do

- [ ] Add useful logging messages
