FROM	ubuntu

RUN	cd /tmp \
&&	apt-get update \
&&	apt-get install -y wget python3\
&&	wget https://raw.githubusercontent.com/dvlromero/Transcriptome_Selector2/master/select_transcriptome.py\
&&	chmod +x select_transcriptome.py \
&&	cp -r * /usr/local/bin \
&&	cd / \
&&	apt autoremove -y wget \
&&	rm -rf /tmp/* \
&&	rm -rf /var/lib/apt/list/*

LABEL	tool=filerename version=0.1.1

WORKDIR /data
