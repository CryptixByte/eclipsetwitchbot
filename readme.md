# EMusicBot v0.1

## Overview
A basic twitch chat bot that utilizes the libraries: twitchio v2.8.2, and [PLACEHOLDER]

### How to set up the bot (Windows)
- getting twitchio with venv
  - cd [location of folder]
  - py -m venv venv
  - venv\Scripts\activate
  - py -m pip install twitchio==2.8.2


### Features
- Basic AutoMod features (Future)
- Several Basic Bot Commands 
- Song Requests (Future)

#### Development Notes

- Used 'curl -H "Client-ID: [Client ID]" -H "Authorization: Bearer [OAuth Token]" "https://api.twitch.tv/helix/users?login=emusicbot"' to get my Bot ID

- https://id.twitch.tv/oauth2/authorize?client_id=zpdbffu9rc3ps3ocrt5pm3lppzxq9i&redirect_uri=http://localhost&response_type=token&scope=chat:read+chat:edit


- Used 'curl -H "Client-ID: dkoikn7irbd5l2zlwl1x6xzhxvmfoi" -H "Authorization: Bearer zpdbffu9rc3ps3ocrt5pm3lppzxq9i" "https://api.twitch.tv/helix/users?login=emusicbot"'
