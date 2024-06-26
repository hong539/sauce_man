# sauce_man

sauce_man is a discord bot to wrapper the search feature for who want make some records or fix the broken preview from some outside URLs.

## To-do-list

### working

* update Dockerfile
* migrage from pyenv+pipenv to pyenv+poetry
* test discord.py
* find a better and safe way to set env
* make app_commands
    * ~~search history messages from a specific channel~~
    * dump history messages from a specific channel
        * calculate the range <= 100 for iterator to append all history to the stored list

### pending

* podman container crashed
    * socket.gaierror: [Errno -2] Name or service not known
* Container part
    * ~~prepare Dockerfile~~
    * ~~Run with podman~~
    * docekr network DNS resovle error
        * ERROR: failed to solve: docker.io/python:3.11.4-slim-bullseye: failed to do request: Head "https://registry-1.docker.io/v2/library/python/manifests/3.11.4-slim-bullseye": EOF

### done

* ~~separate function load_config from class or not? (Hint: Like django settings.py)~~
* ~~postgresql db init~~

## quick-start

```shell
#setting up python version
pyenv local 3.11.4

#Specify which version of Python virtualenv should use.
pipenv --python 3.11.4

#Spawns a shell within the virtualenv.
pipenv shell

#packages
pipenv install discord.py
pipenv install PyYAML
pipenv install pandas
pipenv install SQLAlchemy
pipenv install psycopg2

#run this bot
cd src/
python3 main.py

#freeze requirements.txt
pipenv requirements > requirements.txt

#docker container build/run
docker build . -t docker.io/focal1119/sauce_man:test
docker run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test

#docker compose
#up and run in background
docker compose up -d

#down
docker compose down

#podman container build/run
podman build . -t docker.io/focal1119/sauce_man:test
podman build . --no-cache -t docker.io/focal1119/sauce_man:test
podman run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test
```

## misc

* [how-do-i-apply-environment-variables-to-python-interactive](https://stackoverflow.com/questions/73858371/how-do-i-apply-environment-variables-to-python-interactive)
* [pprint](https://docs.python.org/3.11/library/pprint.html)
* [os.environ](https://docs.python.org/3/library/os.html#os.environ)
* [sqlalchemy/postgresql](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)
* [pandas](https://pandas.pydata.org/)
* [decorator](https://docs.python.org/3/glossary.html#term-decorator)
* [await fetch_message](https://discordpy.readthedocs.io/en/latest/api.html#discord.TextChannel.fetch_message)
* [read_message_history](https://discordpy.readthedocs.io/en/latest/api.html?highlight=history#discord.Permissions.read_message_history)
* [async for ... in history](https://discordpy.readthedocs.io/en/latest/api.html?highlight=history#discord.User.history)
* [discord.py/examples/](https://github.com/Rapptz/discord.py/tree/master/examples)
* [How to retrieve previous messages with discord.py](https://stackoverflow.com/questions/64995479/how-to-retrieve-previous-messages-with-discord-py)
* [How could I grab all chat messages in a specific channel in a discord server using discord.py?](https://stackoverflow.com/questions/64211658/how-could-i-grab-all-chat-messages-in-a-specific-channel-in-a-discord-server-usi)
* [Community Resources](https://discord.com/developers/docs/topics/community-resources#community-resources)
* [discord.com/developers/docs/getting-started](https://discord.com/developers/docs/getting-started)
* [Discord bot that automatically download images from a channel.](https://www.reddit.com/r/Discord_Bots/comments/pdz8kp/discord_bot_that_automatically_download_images/)
    * [d-logger.py](https://github.com/therealOri/d-logger/blob/main/d-logger.py)
* [discord.py/intro](https://discordpy.readthedocs.io/en/latest/intro.html)
* [events](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
    * [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)
        * [asyncio](https://docs.python.org/3.8/library/asyncio.html)

## Important!!!

== We're Using GitHub Under Protest ==

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open {bug ticket, mailing list thread, etc.} ](INSERT_LINK) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please
[check this resource](INSERT_LINK) for how to send us contributions without
using GitHub directly.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)