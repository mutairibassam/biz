## BizBot
Telegram bot to send [4channel](https://boards.4channel.org/biz/) website deleted thread ids, so you will never miss an opportunity.

### run using docker
```bash
docker pull mutairibassam/biz:v0.2-alpha
docker pull mutairibassam/biz:v0.2-alpha biz
docker run biz
```

### run using docker locally
```bash
docker build -t biz .
docker run biz
```

### run using python

```bash
python app.py
```

### add your secrets
You should add your secrets regardless of any method you followed.

create a new file with `config.yml` name in the root of the project. Paste the below snippet and replace `xxx` with a valid values.

```yml
telegram:
  token: xxxxxxxxxxxxxxxxxxxxxxx
  chat_id: -xxxxxxxx
```

*Note: there is no output, the deleted ids will be sent to your telegram groups automatically.