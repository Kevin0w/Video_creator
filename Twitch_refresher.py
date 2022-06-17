"""
Task: Automatically start watching a twitch stream when it goes live.

Requirements:   Use Chrome/Mozilla browser
                Refresh the page every 10 minutes

"""

from selenium import webdriver
import argparse
import time
import pyautogui


def press_f5():
    pyautogui.hotkey('f5')  # Simulates F5 key press = page refresh


# Opens the link and refreshes it using Chrome like browser from selenium module
def open_url_and_refresh_it(url):
    browser = webdriver.Chrome(executable_path="E:\\Github\\Video_creator\\chromedriver.exe")

    browser.get(url)

    # Refreshes the web page
    browser.refresh()


def main():
    print(f"---------------Script start---------------")

    parser = argparse.ArgumentParser()
    parser.add_argument('--twitch_link', default='https://www.twitch.tv/esl_csgo',
                        help='You can insert a twitch url or leave it blank (it will use '
                             'https://www.twitch.tv/esl_csgo as default).')
    parser.add_argument('--refresh_period', default=10,
                        help='You can put the refresh time (the default value is 10 minutes).')
    args = parser.parse_args()

    twitch_link = args.twitch_link
    refresh_period = args.refresh_period
    page_refresh_counter = 0

    print(f"Opening Twitch URL: {twitch_link}")
    print(f"Refreshing every: {refresh_period} minutes")
    print(f"\n")

    while True:
        # open_url_and_refresh_it(twitch_link)
        page_refresh_counter += 1
        print(f"Refreshed {page_refresh_counter} times")
        print(f"Waiting for {refresh_period} to refresh again")
        press_f5()
        time.sleep(60 * refresh_period)


if __name__ == '__main__':
    main()
