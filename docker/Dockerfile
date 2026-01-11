FROM debian:11

ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências básicas
RUN apt-get update && apt-get install -y \
    asterisk \
    asterisk-dev \
    python3 \
    python3-pip \
    net-tools \
    iproute2 \
    lsof \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Cria diretórios necessários
RUN mkdir -p \
    /etc/asterisk \
    /var/lib/asterisk/agi-bin \
    /var/log/asterisk \
    /var/spool/asterisk

# Permissões para AGI
RUN chmod -R 755 /var/lib/asterisk/agi-bin

# Define volumes persistentes
VOLUME [ \
    "/etc/asterisk", \
    "/var/lib/asterisk/agi-bin", \
    "/var/log/asterisk" \
]

# Exposição padrão (SIP + RTP)
EXPOSE 5060/udp
EXPOSE 10000-20000/udp

# Inicializa o Asterisk em foreground (modo container)
CMD ["asterisk", "-f"]
