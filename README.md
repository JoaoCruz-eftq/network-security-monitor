# Network Security Monitor

## Sobre o projeto

O Network Security Monitor é um projeto acadêmico desenvolvido para demonstrar conceitos básicos de Redes de Computadores, Cybersecurity, análise de logs e controle de versão utilizando Git e GitHub.

O sistema analisa um arquivo de eventos de rede e identifica comportamentos potencialmente suspeitos, como múltiplas tentativas de conexão provenientes do mesmo endereço IP.

## Objetivos

* Demonstrar conceitos básicos de monitoramento de rede;
* Analisar eventos registrados em logs;
* Identificar padrões suspeitos;
* Gerar alertas de segurança;
* Praticar Python;
* Aplicar conceitos de Git e GitHub.

## Tecnologias

* Python 3
* Git
* GitHub
* Markdown

## Funcionamento

O programa lê o arquivo localizado em:

```text
logs/security.log
```

Cada linha representa um evento de rede.

Exemplo:

```text
2026-09-08 10:15:01 | 192.168.1.10 | LOGIN_SUCCESS
2026-09-08 10:15:05 | 192.168.1.50 | LOGIN_FAILED
```

O sistema contabiliza eventos suspeitos por endereço IP.

Quando um IP ultrapassa o limite definido de eventos suspeitos, um alerta é apresentado.

## Exemplo de alerta

```text
[ALERTA] Possível atividade suspeita detectada!
IP: 192.168.1.50
Tentativas suspeitas: 5
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/network-security-monitor.git
```

Entre na pasta:

```bash
cd network-security-monitor
```

Execute o programa:

```bash
python scripts/network_monitor.py
```

## Estrutura

```text
network-security-monitor/
├── README.md
├── requirements.txt
├── .gitignore
├── logs/
│   └── security.log
├── scripts/
│   └── network_monitor.py
├── reports/
│   └── relatorio-incidente.md
└── docs/
    └── arquitetura.md
```

## Conceitos de Git utilizados

Durante o desenvolvimento foram utilizados:

* Repositório;
* Commits;
* Branch;
* Pull Request;
* Merge;
* README;
* Controle de versões.

## Projeto acadêmico

Projeto desenvolvido como atividade prática relacionada à trilha GitHub Foundations.
