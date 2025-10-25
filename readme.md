# EclipseBot v1 - IN DEVELOPMENT

## Overview
A basic twitch chat bot that utilizes the libraries: twitchio v2.8.2, Random, and [PLACEHOLDER]

### Features
- [] Basic AutoMod features (Future)
- [] Several Basic Bot Commands (Still working on some commands)
- [] Song Requests (Future)

### Bot Set Up
- **getting twitchio with venv**
  - Open the terminal
  - Enter 'cd [location of folder]'
  - Enter 'py -m venv venv'
  - Enter 'venv\Scripts\activate'
  - Enter 'py -m pip install twitchio==2.8.2' [^1]
    [^1]: We're currently using 2.8.2 
- **Getting Client ID**
  - A Client ID is given by registering an application on the Twitch Developers Console (https://dev.twitch.tv/console)
- **Getting OAuth Token**
  - Go to your browser copy and paste the link below in the search bar and replace [ClientID] with your Client ID (Including the [])
  - https://id.twitch.tv/oauth2/authorize?client_id=[ClientID]&response_type=token&redirect_uri=http://localhost&scope=chat:read+chat:edit
  - If I remember correctly, the page will ask you to authorize your Twitch account. Click ‘Yes,’ and you’ll find your Twitch OAuth token at the top of the browser’s address bar.
- **Replacing Placeholders In Code**
  - Using a text editor open main.py
  - In the variable token replace [PLACEHOLDER] with your oauth token
  - In the variable client_id replace [PLACEHOLDER] with your client id
  - In the variable nick replace [PLACEHOLDER] with the twitch accounts name that will be associated with your bot
- **Modifying the bot to your liking**
  - Usinig a text editor open main.py
  - Locate the commented sections which are green
  - Delete the lines of code below that commented section to the next section (Leave DO NOT DELETE Alone)

  #### Development Notes

  Not Released Yet










