FROM andrius/asterisk

USER root

# Copia AGIs
COPY agi-bin /var/lib/asterisk/agi-bin

# Copia configs
COPY etc /etc/asterisk

# Normaliza CRLF, permissões e dono
RUN sed -i 's/\r$//' /var/lib/asterisk/agi-bin/*.agi \
 && chown -R asterisk:asterisk /var/lib/asterisk/agi-bin \
 && chmod 750 /var/lib/asterisk/agi-bin \
 && find /var/lib/asterisk/agi-bin -type f -name "*.agi" -exec chmod 750 {} \;

# Sons do ConfBridge (se você usa conf-muted / conf-unmuted)
COPY sounds /var/lib/asterisk/sounds
RUN chown -R asterisk:asterisk /var/lib/asterisk/sounds

USER asterisk
