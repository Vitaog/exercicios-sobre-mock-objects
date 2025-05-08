# Exercício Prático – Mock Object (Qualidade e Testes de Software)

Este projeto é baseado no exercício proposto na disciplina de **Qualidade e Testes de Software** e está dividido em duas partes principais: testes com cobertura total da classe `CustomStack`, e a implementação da classe `NumberAscOrder` com seus respectivos testes.

---

## 📁 Estrutura do Projeto

```
├── src/
│ ├── custom_stack_class.py
│ └── number_asc_order.py 
├── test/
│ ├── custom_stack_test.py 
│ └── number_asc_order_test.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ✅ Parte 1 – Testes da `CustomStack`

- Implementação de testes unitários usando `pytest`.
- Todos os métodos da classe `CustomStack` foram testados.
- **Cobertura de código: 100%** (verificada com `pytest-cov`).
- Foram testados os seguintes comportamentos:
  - Inserção de elementos (`push`)
  - Limite de capacidade da pilha
  - Remoção de elementos (`pop`)
  - Acesso ao topo (`top`)
  - Condições de exceção (pilha vazia ou cheia)
  - Métodos auxiliares como `is_empty()` e `size()`

---

## ✅ Parte 2 – Classe `NumberAscOrder`

- Implementação da classe `NumberAscOrder` com o método `sort()`, que recebe uma `CustomStack` e retorna uma lista ordenada.
- Tratamento para pilha vazia incluído.
- Casos de teste implementados:
  - Pilha com 6 números sorteados aleatoriamente.
  - Pilha de 6 posições vazia.
- Cobertura da classe: **83%**, cobrindo todos os requisitos funcionais.

---

## ▶️ Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente

Windows:

```bash
.\venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os testes com cobertura
```bash
pytest --cov=src --cov-report=term-missing
```