# TryHackMe Notes Generator

> A markdown generator for [TryHackMe](https://tryhackme.com/), inspired by John Hammond

## Usage

1. `pip3 install selenium bs4`

2. Visit [here to download](https://chromedriver.chromium.org/downloads) the corresponding driver for the Chrome browser

3. Extract the executable, and might need to mark the downloaded driver as executable by running `chmod +x /path/to/driver`

4. Run the code with

```bash
python3 gen-notes.py -r linuxfundamentalspart1 -d ./chromedriver.exe --headless
```

| Flags        | Required | Description                                                      |
| ------------ | -------- | ---------------------------------------------------------------- |
| -r, --room   | Yes      | The name of the room in TryHackMe (e.g. linuxfundamentalspart1)  |
| -d, --driver | Yes      | Path to web driver executable (e.g. ./chromedriver.exe)          |
| -o, --output | No       | The path to output the result, defaults to ./name_of_the_room.md |
| -n, --name   | No       | Your name                                                        |
| --headless   | No       | Whether to fetch data in headless mode                           |
