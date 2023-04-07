## BizBot
Telegram bot to send [4channel](https://boards.4channel.org/biz/) website deleted threads, so you will never be behind.

We are currently hosting the bot, so we don't need actually to host it or run it locally unless you have a reason. You are welcome to join [our telegram group](https://t.me/+2bD0oJy7brEyNjBk).

Bot message example:
- Missing id: 54472365
- Subject: getting sued
- Archiver: https://archived.moe/biz/thread/54472365
- http://i.4cdn.org/biz/1680681193997391s.jpg

### Run using docker
```bash
docker pull mutairibassam/biz:v0.2-alpha
docker tag mutairibassam/biz:v0.1-alpha biz
docker run biz
```

### Run using docker locally
```bash
git clone https://github.com/mutairibassam/biz.git
cd biz
docker build -t biz .
docker run biz
```

### Run using python

```bash
git clone https://github.com/mutairibassam/biz.git
cd biz
python app.py
```

### Add your secrets
You should add your secrets regardless of any method you followed.

Create a new file with `config.yml` name in the root of the project. Paste the below snippet and replace `xxx` with valid values.

```yml
telegram:
  token: xxxxxxxxxxxxxxxxxxxxxxx
  chat_id: -xxxxxxxx
```

*Note: there is no output, the deleted ids will be sent to your telegram groups that associated with the chat id automatically.
