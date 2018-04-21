cat config.json # Confirms file exists.
python server.py & # Starts server in background.
python serve.py https://github.com/mdn/beginner-html-site-styled & # Sending git url.

wait %2

ls repo/ & # Confirm the repo folder exists.

wait %3

killall python