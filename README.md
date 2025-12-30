# Proposta de Sistema de Comunicação VoIP de Alta Disponibilidade com Automação Inteligente para Uso em Operações

## Descrição
Este projeto é uma simulação inicial para a disciplina de VoIP, baseado no conceito de RoIP (Radio over IP) usando o software Asterisk e AGI (Asterisk Gateway Interface) para automação. O objetivo é demonstrar um sistema VoIP de alta disponibilidade com inteligência para operações de risco e remotas, simulando comunicação entre rádios embarcados via IP.

- **Tema Original (TCC):** Proposta de um sistema que integra hardware embarcado em rádios para RoIP, com automação para cenários críticos (ex.: resgates, explorações remotas).
- **Escopo da Disciplina:** Implementação rápida e simulada, focando em software (sem hardware real por enquanto). Simula cenários ideais com chamadas VoIP roteadas como "rádios" e automação via scripts AGI.

## Tecnologias Utilizadas
- Asterisk: PBX open-source para VoIP.
- AGI: Interface para scripts de automação (Python/Perl).
- Softphones: Para testes (ex.: Zoiper).
- Ambiente: Ubuntu/Linux (ou Docker para portabilidade).

## Requisitos
- Sistema Operacional: Linux (Ubuntu 20.04+ recomendado).
- Dependências: Asterisk 18+, Python 3 para AGI.
- Ferramentas de Teste: Softphones como Zoiper ou Linphone.

## Instalação e Setup
1. **Instale o Asterisk:**
- sudo apt update
- sudo apt install asterisk
2. **Configure arquivos básicos:**
- Edite `/etc/asterisk/sip.conf` para endpoints SIP.
- Edite `/etc/asterisk/extensions.conf` para dialplan e AGI.
3. **Instale dependências para AGI:**
- sudo apt install python3-asterisk-agi  # Ou similar, dependendo da distro
4. **Clone o repo e rode scripts:**
- git clone https://github.com/PreceptorUgin/Projeto-AGI-Automacao-Inteligente-para-uso-em-operacoes
- cd ./Projeto-AGI-Automacao-Inteligente-para-uso-em-operacoes

# Copie scripts AGI para /var/lib/asterisk/agi-bin/
- sudo asterisk -rx "reload"

## Uso
1. Inicie o Asterisk: `sudo systemctl start asterisk`.
2. Registre softphones nos endpoints configurados.
3. Teste RoIP simulado:
- Ligue de um softphone para extensão configurada (ex.: 100).
- O AGI script automatiza o roteamento (ex.: simula multicast para "grupo de rádios").
4. Simule cenário de risco: Use o script de teste para induzir falhas e ver automação (logs em `/var/log/asterisk/`).

## Backlog e Planejamento
Veja o arquivo [BACKLOG.md](BACKLOG.md) para detalhes de user stories e tasks.

## Limitações
- Esta é uma simulação software; integração com hardware embarcado (ex.: Raspberry Pi em rádios) é para fases futuras.
- Alta disponibilidade é básica (failover scriptado); para produção, use Asterisk em cluster.

## Referências
- Documentação Asterisk: https://wiki.asterisk.org/
- AGI Tutorial: https://www.voip-info.org/asterisk-agi/
- RoIP Conceitos: Artigos sobre Radio over IP em operações críticas.

## Contribuições
Sugestões bem-vindas! Abra issues ou PRs.

Autor: [Seu Nome]  
Data: Dezembro 2025
