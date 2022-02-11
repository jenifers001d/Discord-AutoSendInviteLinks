import threading
import traceback
import requests
import config
import random
import time
import json
import sys


def sendInviteLink(headers, channel):
    content = channel['inviteMessage'] if channel['inviteMessage'] else config.inviteMessage
    channelID = channel['id']

    while True:
        try:
            msg = {
                "content": content,
                "nonce": f"82329451214{random.randrange(0, 1000)}33232234",
                "tts": False,
            }
            url = f"https://discord.com/api/v9/channels/{channelID}/messages"
            res = requests.post(
                url=url, headers=headers, data=json.dumps(msg))
            print(res.content)

        except Exception as e:
            print(f'Error in {channel["name"]}: {e}')
            print(traceback.format_exc())

        time.sleep(random.randint(
            int(config.interval * 0.9), int(config.interval * 1.1)))


def main():
    try:
        for bot in config.bots:
            headers = config.headers
            headers['Authorization'] = bot['token']

            channels = bot['channels'].copy()
            for channel in channels:
                threading.Thread(
                    target=sendInviteLink,
                    args=(headers, channel),
                    daemon=True,
                ).start()
                time.sleep(random.randint(10, 15))

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
