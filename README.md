# Chrome Print Page Python

Trivial scripts that helps me automate printing with chrome.

## Usage

On first terminal start Google Chrome with `./start_chrome.sh`.

On the second terminal invoke script
```
./print_me.py https://google.com
./print_me.py --printBackground True https://bing.com
```

## Requirements

Python 3.6+ and modules from `requirements.txt`

Depedency installation within virtualenv

```
virtualenv -p /usr/bin/python3 venv
. venv/bin/activate
pip install -r requirements.txt 
```

## Documentation

https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-printToPDF

```
./print_with_chrome.py -h
```

## Other solutions

- https://github.com/marty90/PyChromeDevTools - this script uses this great module
- https://github.com/thecodingmachine/gotenberg - "A Docker-powered stateless API for converting HTML, Markdown and Office documents to PDF." For HTML to PDF generation uses Chrome as backend.
