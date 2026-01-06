# Proposta de Sistema de Comunicação VoIP em Grupos com Controle de Prioridade e Automação via AGI

## Descrição
Este projeto propõe a implementação de uma central de comunicação VoIP baseada no Asterisk, com automação por meio da Asterisk Gateway Interface (AGI), orientada ao modelo de comunicação estilo rádio (walkie-talkie) sobre IP. O sistema é concebido para operar com múltiplos grupos de comunicação isolados, permitindo que diferentes equipes utilizem a mesma central VoIP simultaneamente, sem interferência entre os grupos.

O acesso ao sistema é realizado por meio de softphones em dispositivos móveis, que simulam rádios IP. Dentro de cada grupo, o áudio transmitido por um participante é distribuído de forma uniforme para todos os demais membros do grupo. O controle do fluxo de fala é realizado por meio de uma fila de prioridade, garantindo que apenas um usuário transmita por vez, preservando o modelo half-duplex típico de sistemas de rádio e evitando colisões de áudio.

O projeto foi idealizado de forma incremental, permitindo a adição de novas funcionalidades ao longo do tempo, sem a necessidade de reestruturação completa da arquitetura.

- Tema original (projeto ampliado): desenvolvimento de um sistema RoIP com integração a hardware embarcado em rádios, automação inteligente e controle de prioridade para uso em operações críticas e ambientes remotos.
- Escopo da disciplina: implementação funcional e simulada em software, com foco na comunicação VoIP em grupos isolados, automação via AGI, controle de prioridade de transmissão e monitoramento básico, sem integração com hardware físico nesta fase.

## Objetivos
- Implementar comunicação VoIP em modo half-duplex, simulando o funcionamento de sistemas de rádio.
- Permitir a criação e operação simultânea de múltiplos grupos de comunicação isolados.
- Garantir que o áudio de um transmissor seja entregue de forma igual a todos os participantes do grupo.
- Controlar o acesso à transmissão por meio de filas de prioridade, evitando sobreposição de falas.
- Automatizar regras de controle, sessão e registro de eventos utilizando AGI.
- Disponibilizar uma base arquitetural preparada para futuras expansões e melhorias.

## Arquitetura Geral
O sistema é organizado de forma modular, separando claramente o plano de mídia do plano de controle, conforme o diagrama conceitual a seguir:

Softphones (Dispositivos Móveis)
        |
       SIP
        |
     Asterisk
  [Dialplan + Bridges]
        |
       AGI
        |
 Camada de Controle e Estado
        |
 Interface Web Administrativa

O Asterisk é responsável pelo tratamento de chamadas e fluxo de mídia (RTP), enquanto o AGI atua como camada de controle, gerenciando prioridades, estados de grupo e registro de eventos. A interface web consome informações geradas pela camada de controle para fins de monitoramento e administração.

## Funcionamento dos Grupos de Comunicação
Cada grupo de comunicação é tratado como uma entidade lógica independente dentro da central. Usuários pertencentes a um grupo compartilham o mesmo fluxo de áudio durante uma transmissão ativa. O sistema adota as seguintes premissas operacionais:

- Apenas um usuário pode transmitir áudio por vez dentro de um grupo.
- As solicitações de transmissão são organizadas em uma fila de prioridade.
- O usuário no topo da fila recebe permissão para transmitir.
- Os demais participantes permanecem em modo de escuta até a liberação do canal.
- O controle de transmissão pode ser acionado por DTMF, simulando o comportamento de um botão PTT (Push-To-Talk).

Esse modelo garante previsibilidade no fluxo de comunicação e evita interferências ou sobreposição de áudio.

## Tecnologias Utilizadas
- Asterisk: PBX open-source para gerenciamento de chamadas VoIP.
- AGI: Interface de automação utilizada para controle de sessões, prioridades e eventos.
- Softphones SIP: clientes utilizados em dispositivos móveis para simulação de rádios IP (ex.: Zoiper, Linphone).
- Interface Web Administrativa: responsável pelo monitoramento e gerenciamento do sistema.
- Ambiente de Execução: Linux (Ubuntu 20.04 ou superior), com possibilidade de uso de containers Docker para portabilidade.

## Requisitos
- Sistema Operacional: Linux (Ubuntu 20.04 ou superior).
- Asterisk: versão 18 LTS ou superior.
- Linguagem para scripts AGI: Python 3 ou equivalente.
- Softphones compatíveis com o protocolo SIP.

## Instalação e Setup
1. Instalar o Asterisk no sistema operacional:
   - sudo apt update
   - sudo apt install asterisk

2. Configurar os arquivos básicos do Asterisk:
   - Definição dos endpoints SIP (sip.conf ou pjsip.conf).
   - Configuração do dialplan (extensions.conf) para direcionamento das chamadas aos grupos.
   - Associação de scripts AGI às extensões responsáveis pelo controle das sessões.

3. Instalar dependências para execução dos scripts AGI:
   - sudo apt install python3

4. Clonar o repositório do projeto e realizar o deploy:
   - git clone https://github.com/PreceptorUgin/Projeto-AGI-Automacao-Inteligente-para-uso-em-operacoes
   - Copiar os scripts AGI para o diretório /var/lib/asterisk/agi-bin/
   - Ajustar permissões de execução dos scripts
   - Recarregar as configurações do Asterisk com:
     - sudo asterisk -rx "reload"

## Uso do Sistema
1. Iniciar o serviço do Asterisk.
2. Registrar os softphones nos endpoints SIP configurados.
3. Conectar-se à extensão associada a um grupo de comunicação.
4. Utilizar o comando de transmissão (PTT) para solicitar acesso à fala.
5. O AGI processa a solicitação, gerencia a fila de prioridade e libera a transmissão conforme as regras definidas.
6. Durante a transmissão, o áudio é distribuído igualmente para todos os membros do grupo.
7. Eventos e sessões são registrados em logs para fins de monitoramento e auditoria.

## Interface Administrativa
A interface gráfica do sistema tem como função primordial:

- Monitorar a atividade dos grupos de comunicação.
- Visualizar usuários conectados em cada grupo.
- Identificar o participante que está transmitindo no momento.
- Acessar logs de eventos, transmissões e sessões.
- Gerenciar parâmetros básicos dos grupos e usuários.

## Backlog e Planejamento
O projeto foi estruturado para permitir evolução contínua. Funcionalidades previstas para etapas futuras incluem:

- Definição de níveis de prioridade por usuário ou função.
- Gravação de transmissões por grupo.
- Integração com rádios físicos e hardware embarcado.
- Implementação de criptografia de mídia (SRTP).
- Controle avançado de permissões e autenticação.
- Coleta de métricas de desempenho e uso.

Detalhes adicionais encontram-se descritos no arquivo BACKLOG.md.

## Limitações
- Implementação restrita ao ambiente de simulação em software.
- Ausência de integração direta com hardware de rádio nesta fase.
- Mecanismos de alta disponibilidade limitados ao contexto acadêmico.

## Referências
- Documentação oficial do Asterisk.
- Documentação da Asterisk Gateway Interface (AGI).
- Artigos e publicações sobre conceitos de Radio over IP (RoIP) aplicados a operações críticas.

Autor: Júlio Souza, Pedro Henrique, Magnus Jr.
Instituição: IFRN – Campus Natal Central
Disciplina: VoIP
Data: Janeiro de 2026
