# EclipseBot v1

## Overview
A basic twitch chat bot that utilizes the libraries: twitchio v2.8.2, Random, and [PLACEHOLDER]

### Features
- Basic AutoMod features (Future)
- Several Basic Bot Commands 
- Song Requests (Future)

### Bot Set Up
- **getting twitchio with venv**
  - cd [location of folder]
  - py -m venv venv
  - venv\Scripts\activate
  - py -m pip install twitchio==2.8.2

- **Getting OAuth Token**
  - A Client ID is given by registering an application on the Twitch Developers Console (https://dev.twitch.tv/console)
  - Go to your browser and enter the link below while replacing [ClientID] with your Client ID (Including the [])
  - https://id.twitch.tv/oauth2/authorize?client_id=[ClientID]&response_type=token&redirect_uri=http://localhost&scope=chat:read+chat:edit






