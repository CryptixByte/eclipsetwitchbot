# EclipseBot v1 - IN DEVELOPMENT

## Overview
A basic twitch chat bot that utilizes the libraries: twitchio v2.8.2, Random, and [PLACEHOLDER]

### Features
- Basic AutoMod features (Future)
- Several Basic Bot Commands 
- Song Requests (Future)

### Bot Set Up
- **getting twitchio with venv**
  - Open the terminal
  - Enter 'cd [location of folder]'
  - Enter 'py -m venv venv'
  - Enter 'venv\Scripts\activate'
  - Enter 'py -m pip install twitchio==2.8.2'
    - We're currently using 2.8.2 

- **Getting OAuth Token**
  - A Client ID is given by registering an application on the Twitch Developers Console (https://dev.twitch.tv/console)
  - Go to your browser and enter the link below while replacing [ClientID] with your Client ID (Including the [])
  - https://id.twitch.tv/oauth2/authorize?client_id=[ClientID]&response_type=token&redirect_uri=http://localhost&scope=chat:read+chat:edit








