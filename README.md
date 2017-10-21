# MeeTube: Music Bot, look at me!
![GitHub Logo](https://i.imgur.com/o8ZAQz4.png)
MeeTube is an open-source <b>telegram bot that gets songs</b> from YouTube for you.

You can speak with him [here!](https://t.me/MeeTubeBot)

## Dependencies

To run the bot, you'll need <b>python 3</b> installed with a few modules:
#### telegram
```$ pip3 install python-telegram-bot --upgrade```
#### beautiful soup
```$ pip3 install bs4 --upgrade```
#### lxml
```$ pip3 install lxml --upgrade```
#### youtube_dl
```$ pip3 install youtube_dl --upgrade```
#### ffprobe
Then, for the functionality of getting the song together, you're gonna need <b>ffprobe</b>, part of the <b>ffmpeg package</b>:

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
