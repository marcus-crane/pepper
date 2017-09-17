# pepper

A script for downloading PEPs.

I was going to start reading PEP 0008 uhh *looks at watch* like 4 hours ago but I kinda wished they were available as PDFs but without the extra rubbish intended for websites.

PDFs also like to strip out a lot of the nice styling which, I dunno, I quite like the Python CSS.

Anyway, this thing just merges the PEP content with some template styling and renders a nice fresh HTML page. It's basically the Python.org CSS dumped into a template and some small tweaks added. Majority of it probably isn't needed but It Works™

## Usage

You'll need to install the following Python libraries and a Python 3 installation:

```
pip3 install beautifulsoup4 mako requests
```

and then run the script like so:

```
python3 pepper.py 0008
```

Replace `python3` (and pip3) with whatever your Python 3 install is named. For Linux flavours, it's likely just `python` while for macOS users, it'll be symlinked as `python3` when installed using `brew`.

## Why not just use the peps repository on Github

Yeahhhh, I did see that. The plain text was ok but it didn't feel as nice to read as the PEPs on the site which is just me being needlessly picky. It did also allow generation of HTML but the styles seemed all wonky and not like what I was expecting.

I figured it was just as quick to whip up something of my own, plus it meant getting more Python practice in 😎