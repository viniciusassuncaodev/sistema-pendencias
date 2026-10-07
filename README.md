# Sistema de Controle de Pendências

Sistema desktop simples feito em Python com Tkinter para cadastro e controle de pendências, com tela de login e persistência dos dados em arquivo JSON.

## Funcionalidades

- Tela de login (usuário/senha)
- Tela principal do sistema
- Cadastro de nova pendência (descrição + responsável)
- Listagem das pendências cadastradas
- Salvamento automático em `pendencias.json`

## Tecnologias

- Python 3
- Tkinter (interface gráfica)
- JSON (persistência dos dados)

## Como executar

```bash
python sistema_pendencias.py
```

**Login de teste (apenas para demonstração):**
- Usuário: `admin`
- Senha: `123`

## Próximos passos

- Buscar pendências por responsável
- Marcar pendência como concluída
- Migrar o armazenamento para SQLite
- Trocar o login fixo por autenticação real