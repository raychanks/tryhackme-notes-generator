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

---

## Sample output

    # linuxfundamentalspart1

    > 1337 | 14 September, 2021

    ---

    # Task 1 - Introduction

    > Let's get started!

    ```

    ```

    # Task 2 - A Bit of Background on Linux

    > Research: What year was the first release of a Linux operating system?

    ```

    ```

    # Task 3 - Interacting With Your First Linux Machine (In-Browser)

    > I've deployed my first Linux machine!

    ```

    ```

    # Task 4 - Running Your First few Commands

    > If we wanted to output the text "TryHackMe", what would our command be?

    ```

    ```

    > What is the username of who you're logged in as on your deployed Linux machine?

    ```

    ```

    # Task 5 - Interacting With the Filesystem!

    > On the Linux machine that you deploy, how many folders are there?

    ```

    ```

    > Which directory contains a file?

    ```

    ```

    > What is the contents of this file?

    ```

    ```

    > Use the cd command to navigate to this file and find out the new current working directory. What is the path?

    ```

    ```

    # Task 6 - Searching for Files

    > Use grep on "access.log" to find the flag that has a prefix of "THM". What is the flag?

    ```

    ```

    > And I still haven't found what I'm looking for!

    ```

    ```

    # Task 7 - An Introduction to Shell Operators

    > If we wanted to run a command in the background, what operator would we want to use?

    ```

    ```

    > If I wanted to replace the contents of a file named "passwords" with the word "password123", what would my command be?

    ```

    ```

    > Now if I wanted to add "tryhackme" to this file named "passwords" but also keep "passwords123", what would my command be

    ```

    ```

    > Now use the deployed Linux machine to put these into practice

    ```

    ```

    # Task 8 - Conclusions & Summaries

    > I'll have a play around!

    ```

    ```

    # Task 9 - Linux Fundamentals Part 2

    > Terminate the machine deployed in this room from task 3.

    ```

    ```

    > Join Linux Fundamentals Part 2!

    ```

    ```
