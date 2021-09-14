#! /usr/bin/env python3

import argparse
from bs4 import BeautifulSoup
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import sys


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--room",
        help="The room name of TryHackMe (e.g. linuxfundamentalspart1)",
        required=True,
    )
    parser.add_argument(
        "-d",
        "--driver",
        help="Path to web driver executable (e.g. ./chromedriver.exe)",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The path to output the result, defaults to ./name_of_the_room.md",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Your name",
        default="1337"
    )
    parser.add_argument(
        "--headless",
        help="Whether to fetch data in headless mode",
        action='store_true'
    )
    args = parser.parse_args()

    if args.output == None:
        args.output = f"{args.room}.md"

    web_driver_executable = Path(args.driver)
    if not web_driver_executable.is_file():
        print("[!] incorrect path to web driver executable")
        sys.exit(1)

    return args


class WebScraper:
    def __init__(self, args):
        options = webdriver.ChromeOptions()

        if args.headless:
            options.add_argument("--headless")

        self.args = args
        self.driver = webdriver.Chrome(
            options=options,
            executable_path=args.driver,
        )

    def get_web_content(self):
        if self.args.headless:
            print("[+] Fetching data in headless mode, this might take a while...")

        self.driver.get('https://tryhackme.com/room/' + self.args.room)

        task_element_wrapper = self.wait_for_element(
            self.driver, '#taskContent')
        content = task_element_wrapper.get_attribute('innerHTML')

        tasks = self.parse_html(content)

        if len(tasks) == 0:
            print("[!] Cannot get room data, please double check the name of the room")
            sys.exit(1)

        return tasks

    def parse_html(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        tasks = []

        for el in soup.find_all(class_='card'):
            _, task_title = el.a.get_text().strip().split("  ")
            task = {
                "title": task_title,
                "sub_tasks": [],
            }

            questions = el.find(
                class_="card-body"
            ).find_all(class_="room-task-questions")

            for q in questions:
                task["sub_tasks"].append(q.get_text().strip())

            tasks.append(task)

        return tasks

    def wait_for_element(self, driver, selector):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, selector)
            )
        )


class NoteGenerator:
    def __init__(self, args):
        self.args = args

    def write_markdown(self, data):
        today = date.today()
        markdown = f"# {self.args.room}\n\n> {self.args.name} | {today.strftime('%d %B, %Y')}\n\n---\n\n"

        for idx, task in enumerate(data):
            title = task["title"]
            task_num = idx + 1
            markdown += f"# Task {task_num} - {title}\n\n"

            for question in task["sub_tasks"]:
                markdown += f"> {question}\n\n"
                markdown += "```\n\n```\n\n"

        f = open(self.args.output, "w")
        f.write(markdown)
        f.close()


def main():
    args = get_args()

    scraper = WebScraper(args)
    content = scraper.get_web_content()

    note_generator = NoteGenerator(args)
    note_generator.write_markdown(content)


if __name__ == "__main__":
    main()
