inviteMessage = "Hi\n請點擊邀請連結\n救救可憐人\nhttps://discord.gg/Ewj3G6Hh"
interval = 1800  # 1800 seconds = 30 minutes 設定多久重發一次

# Bot settings
bots = [
    {
        'name': 'bot1',  # Bot name
        # Discord auth token
        'token': '放入你的授權令牌 PutYourAuthorizationToken',
        'channels': [
            {
                'name': 'WTC - nft邀請連結互助',  # Channel name
                'id': '932206080338047007',  # Channel ID
                'inviteMessage':  "Hi\n請輸入想客製化的內容"
            },
            {
                'name': 'NTF白名單工具群 - nft邀請互助',
                'id': '932118385741942834',
                'inviteMessage':  ""  # 不想輸入客製化就刪掉這行，或是雙引號中留白
            },
            {
                'name': 'LoreneJen - shillzone',
                'id': '933283701150842880',
            },
            {
                'name': '羊駝 - shilling',
                'id': '892731422513713222',
            },
            {
                'name': 'Shark Doo Doo - shill',
                'id': '940373896140558346',
            },
            {
                'name': '呢喃貓 - nft-推薦碼連結',
                'id': '928554021353037846',
            },
        ],
    },
]


# Advanced settings - do not modify unless you know what you're doing
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
    'Pragma': 'no-cache',
    'Origin': 'https://discord.com',
    'Referer': 'https://discord.com/channels/@me',
    'Sec-Ch-Ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76',
    'X-Debug-Options': 'bugReporterEnabled',
    'X-Discord-Locale': 'zh-TW',
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InpoLVRXIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk3LjAuNDY5Mi45OSBTYWZhcmkvNTM3LjM2IEVkZy85Ny4wLjEwNzIuNzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Ny4wLjQ2OTIuOTkiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEzMTk0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
}
