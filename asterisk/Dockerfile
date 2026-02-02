FROM debian:12

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
  build-essential \
  git \
  wget \
  libncurses5-dev \
  libssl-dev \
  libxml2-dev \
  uuid-dev \
  libsqlite3-dev \
  libjansson-dev \
  libedit-dev \
  libsndfile1-dev \
  libcurl4-openssl-dev \
  libopus-dev \
  libpjproject-dev \
  ca-certificates \
  python3 \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src

RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-22-current.tar.gz \
 && tar xzf asterisk-22-current.tar.gz \
 && cd asterisk-22* \
 && ./configure \
 && make menuselect.makeopts \
 && menuselect/menuselect \
    --enable app_confbridge \
    --enable res_confbridge \
    --enable bridge_softmix \
    menuselect.makeopts \
 && make -j$(nproc) \
 && make install \
 && make samples \
 && make config

RUN useradd -r -d /var/lib/asterisk -s /sbin/nologin asterisk \
 && chown -R asterisk:asterisk /var/lib/asterisk /var/log/asterisk /var/spool/asterisk

USER asterisk
CMD ["/usr/sbin/asterisk", "-f"]

