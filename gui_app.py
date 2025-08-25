import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
from dotenv import load_dotenv
from bybit_p2p import P2P

# Carrega variáveis do arquivo .env
load_dotenv()

class BybitP2PGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Bybit P2P Manager")
        self.root.geometry("800x600")
        
        self.api = None
        self.setup_ui()
    
    def setup_ui(self):
        # Frame de configuração
        config_frame = ttk.LabelFrame(self.root, text="Configuração API", padding=10)
        config_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(config_frame, text="API Key:").grid(row=0, column=0, sticky="w")
        self.api_key_entry = ttk.Entry(config_frame, width=50, show="*")
        self.api_key_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(config_frame, text="API Secret:").grid(row=1, column=0, sticky="w")
        self.api_secret_entry = ttk.Entry(config_frame, width=50, show="*")
        self.api_secret_entry.grid(row=1, column=1, padx=5)
        
        self.testnet_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(config_frame, text="Testnet", variable=self.testnet_var).grid(row=2, column=0, sticky="w")
        
        ttk.Button(config_frame, text="Conectar", command=self.connect_api).grid(row=2, column=1, sticky="e")
        
        # Frame de ações
        actions_frame = ttk.LabelFrame(self.root, text="Ações", padding=10)
        actions_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(actions_frame, text="Ver Saldo", command=self.get_balance).pack(side="left", padx=5)
        ttk.Button(actions_frame, text="Listar Anúncios", command=self.get_ads).pack(side="left", padx=5)
        ttk.Button(actions_frame, text="Pedidos Pendentes", command=self.get_pending_orders).pack(side="left", padx=5)
        
        # Área de resultados
        results_frame = ttk.LabelFrame(self.root, text="Resultados", padding=10)
        results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=20)
        self.results_text.pack(fill="both", expand=True)
    
    def connect_api(self):
        api_key = self.api_key_entry.get() or os.getenv("BYBIT_API_KEY")
        api_secret = self.api_secret_entry.get() or os.getenv("BYBIT_API_SECRET")
        
        if not api_key or not api_secret:
            messagebox.showerror("Erro", "API Key e Secret são obrigatórios")
            return
        
        try:
            self.api = P2P(
                testnet=self.testnet_var.get(),
                api_key=api_key,
                api_secret=api_secret
            )
            messagebox.showinfo("Sucesso", "Conectado à API!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na conexão: {str(e)}")
    
    def get_balance(self):
        if not self.api:
            messagebox.showerror("Erro", "Conecte-se à API primeiro")
            return
        
        try:
            balance = self.api.get_current_balance(accountType="FUND", coin="USDT")
            self.show_result("Saldo", balance)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao obter saldo: {str(e)}")
    
    def get_ads(self):
        if not self.api:
            messagebox.showerror("Erro", "Conecte-se à API primeiro")
            return
        
        try:
            ads = self.api.get_ads_list()
            self.show_result("Anúncios", ads)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao obter anúncios: {str(e)}")
    
    def get_pending_orders(self):
        if not self.api:
            messagebox.showerror("Erro", "Conecte-se à API primeiro")
            return
        
        try:
            orders = self.api.get_pending_orders()
            self.show_result("Pedidos Pendentes", orders)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao obter pedidos: {str(e)}")
    
    def show_result(self, title, data):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"=== {title} ===\n\n")
        self.results_text.insert(tk.END, str(data))

if __name__ == "__main__":
    root = tk.Tk()
    app = BybitP2PGui(root)
    root.mainloop()