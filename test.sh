cat config.json # Confirms file exists.
python server.py & # Starts server in background.

sleep 5 # Wait

python serve.py https://github.com/mdn/beginner-html-site-styled & # Sending git url.

sleep 5 # Wait

ls repo/ # Confirm the repo folder exists.