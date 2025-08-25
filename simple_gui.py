import tkinter as tk
from tkinter import ttk, messagebox
import os
from dotenv import load_dotenv

load_dotenv()

class SimpleBybitGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Bybit P2P - Configuracao")
        self.root.geometry("600x400")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)
        
        # Titulo
        title_label = ttk.Label(main_frame, text="Bybit P2P Manager", font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Status da API
        status_frame = ttk.LabelFrame(main_frame, text="Status da Conexao", padding=10)
        status_frame.pack(fill="x", pady=(0, 20))
        
        api_key = os.getenv("BYBIT_API_KEY", "Nao configurada")
        api_secret = os.getenv("BYBIT_API_SECRET", "Nao configurada")
        
        ttk.Label(status_frame, text=f"API Key: {api_key[:10]}..." if len(api_key) > 10 else f"API Key: {api_key}").pack(anchor="w")
        ttk.Label(status_frame, text=f"API Secret: {'*' * 10 if api_secret != 'Nao configurada' else api_secret}").pack(anchor="w")
        
        # Problema detectado
        problem_frame = ttk.LabelFrame(main_frame, text="Problema Detectado", padding=10)
        problem_frame.pack(fill="x", pady=(0, 20))
        
        problem_text = """ERRO: IP nao autorizado (ErrCode: 10010)

Sua API key esta restrita por endereco IP.

Para resolver:
1. Acesse sua conta Bybit
2. Va em API Management
3. Edite sua API key
4. Adicione seu IP atual ou remova restricoes de IP
5. Ou crie uma nova API key sem restricoes"""
        
        ttk.Label(problem_frame, text=problem_text, justify="left").pack(anchor="w")
        
        # Botoes
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(20, 0))
        
        ttk.Button(button_frame, text="Testar Conexao", command=self.test_connection).pack(side="left", padx=(0, 10))
        ttk.Button(button_frame, text="Abrir Bybit API", command=self.open_bybit_api).pack(side="left")
    
    def test_connection(self):
        try:
            from bybit_p2p import P2P
            
            api = P2P(
                testnet=False,
                api_key=os.getenv("BYBIT_API_KEY"),
                api_secret=os.getenv("BYBIT_API_SECRET")
            )
            
            # Tenta uma chamada simples
            result = api.get_account_information()
            messagebox.showinfo("Sucesso", "Conexao estabelecida com sucesso!")
            
        except Exception as e:
            error_msg = str(e)
            if "10010" in error_msg:
                messagebox.showerror("Erro de IP", "IP nao autorizado. Configure sua API key no Bybit.")
            elif "10003" in error_msg:
                messagebox.showerror("Erro de Credenciais", "API key ou secret invalidos.")
            else:
                messagebox.showerror("Erro", f"Erro: {error_msg}")
    
    def open_bybit_api(self):
        import webbrowser
        webbrowser.open("https://www.bybit.com/app/user/api-management")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBybitGui(root)
    root.mainloop()