# MeeTube: Music Bot, look at me!
![GitHub Logo](https://i.imgur.com/o8ZAQz4.png)
<br>
MeeTube is an open-source <b>telegram bot that gets songs</b> from YouTube for you.

You can speak with him [here!](https://t.me/MeeTubeBot)

<i>People reported that it doesn't work on iOS. Update coming to fix that.</i>

## Dependencies

To run the bot, you'll need <b>python 3</b> installed with a few modules:

```
python-telegram-bot
requests
bs4
lxml
youtube_dl
```
#### ffprobe
We'll also need <b>ffprobe</b>, dependency of `youtube_dl`, and part of the <b>ffmpeg package</b>:

```sudo apt-get update```

```sudo apt-get install ffmpeg```

## Running and deploying
To run the bot, simply run:

```python3 bot.py```

And to keep it always running on your machine, you should run using <b>screen</b>:
##### Create a screen:
```screen -S nameofscreen```

##### Start the bot:
```python3 bot.py```

##### Detach from screen (or simply close the terminal window)
```'CTRL + A' + 'D'```
