# READMEがないのでここに書きます。（READMEは必ず用意しましょう）
# ローカルでDBはどうやって構築してます？DB用のDockerfileが見当たらず...（Slackなどで教えてください）
FROM postgres:14

# Time ZoneAc
ENV TZ Asia/Tokyo

# Language
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8