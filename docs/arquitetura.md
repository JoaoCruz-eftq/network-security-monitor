# Arquitetura do Projeto

## Visão geral

O Monitor de Segurança de Rede foi desenvolvido para analisar eventos registrados em logs e identificar possíveis atividades suspeitas.

## Fluxo do sistema

```text
Arquivo de logs
      |
      v
Leitura dos eventos
      |
      v
Análise dos eventos
      |
      v
Agrupamento por IP
      |
      v
Identificação de atividades suspeitas
      |
      v
Geração de alertas
