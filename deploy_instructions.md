# Deploy no Servidor

## 1. Instalar dependências:
```bash
pip install -r requirements.txt
```

## 2. Configurar credenciais:
- O arquivo `.env` já está configurado com suas credenciais
- Certifique-se que o IP do servidor está liberado na API key

## 3. Testar conexão:
```bash
python quick_test.py
```

## 4. Executar interface gráfica:
```bash
python gui_app.py
```

## 5. Ou usar interface simplificada:
```bash
python simple_gui.py
```

## Arquivos importantes:
- `.env` - Credenciais (já configurado)
- `quick_test.py` - Teste rápido da API
- `gui_app.py` - Interface completa
- `simple_gui.py` - Interface simplificada com diagnósticos