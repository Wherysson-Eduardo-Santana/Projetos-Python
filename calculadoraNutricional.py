import tkinter as tk
from tkinter import messagebox

class NutritionalCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Valor Nutricional")
        
        self.ingredientes = {}
        
        ###Labels e Entradas para Ingredientes
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nome do Ingrediente:").grid(row=0, column=0, padx=10, pady=5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Quantidade (g):").grid(row=1, column=0, padx=10, pady=5)
        self.quantidade_entry = tk.Entry(self.root)
        self.quantidade_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Calorias (por 100g):").grid(row=2, column=0, padx=10, pady=5)
        self.calorias_entry = tk.Entry(self.root)
        self.calorias_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Carboidratos (por 100g):").grid(row=3, column=0, padx=10, pady=5)
        self.carboidratos_entry = tk.Entry(self.root)
        self.carboidratos_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Proteínas (por 100g):").grid(row=4, column=0, padx=10, pady=5)
        self.proteinas_entry = tk.Entry(self.root)
        self.proteinas_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Gorduras (por 100g):").grid(row=5, column=0, padx=10, pady=5)
        self.gorduras_entry = tk.Entry(self.root)
        self.gorduras_entry.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Gorduras Saturadas (por 100g):").grid(row=6, column=0, padx=10, pady=5)
        self.gorduras_saturadas_entry = tk.Entry(self.root)
        self.gorduras_saturadas_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Adicionar Ingrediente", command=self.add_ingredient).grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="Calcular Valor Nutricional", command=self.calculate_nutrition).grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="Sair", command=self.root.quit).grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    ###Declaração das variaveis 

    def add_ingredient(self):
        try:
            nome = self.nome_entry.get().strip()
            quantidade = float(self.quantidade_entry.get().strip())
            calorias = float(self.calorias_entry.get().strip())
            carboidratos = float(self.carboidratos_entry.get().strip())
            proteinas = float(self.proteinas_entry.get().strip())
            gorduras = float(self.gorduras_entry.get().strip())
            gorduras_saturadas = float(self.gorduras_entry.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
            return
        
        if nome in self.ingredientes:
            messagebox.showwarning("Aviso", "Ingrediente já adicionado.")
            return
        
        self.ingredientes[nome] = {
            'quantidade': quantidade,
            'calorias': calorias * quantidade / 100,
            'carboidratos': carboidratos * quantidade / 100,
            'proteinas': proteinas * quantidade / 100,
            'gorduras': gorduras * quantidade / 100,
            'gorduras saturadas': gorduras_saturadas * quantidade / 100
        }
        
        messagebox.showinfo("Sucesso", "Ingrediente adicionado com sucesso!")
        self.clear_entries()

    def clear_entries(self):
        self.nome_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)
        self.calorias_entry.delete(0, tk.END)
        self.carboidratos_entry.delete(0, tk.END)
        self.proteinas_entry.delete(0, tk.END)
        self.gorduras_entry.delete(0, tk.END)
        self.gorduras_saturadas_entry.delete(0, tk.END)

    def calculate_nutrition(self):
        if not self.ingredientes:
            messagebox.showwarning("Aviso", "Nenhum ingrediente foi adicionado.")
            return
        
        calorias_totais = sum(ingrediente['calorias'] for ingrediente in self.ingredientes.values())
        carboidratos_totais = sum(ingrediente['carboidratos'] for ingrediente in self.ingredientes.values())
        proteinas_totais = sum(ingrediente['proteinas'] for ingrediente in self.ingredientes.values())
        gorduras_totais = sum(ingrediente['gorduras'] for ingrediente in self.ingredientes.values())
        gorduras_saturadas = sum(ingrediente['gorduras'] for ingrediente in self.ingredientes.values())

        ###Dividindo os totais por 50
        calorias_totais /= 50
        carboidratos_totais /= 50
        proteinas_totais /= 50
        gorduras_totais /= 50
        gorduras_saturadas /= 50

        resultado = (
            f"\nInformação Nutricional Total\n"
            f"PORÇÃO 50g\n"
            f"(Equivalente a 2 fatias)\n"
            f"Calorias: {calorias_totais:.2f} kcal\n"
            f"Carboidratos: {carboidratos_totais:.2f} g\n"
            f"Proteínas: {proteinas_totais:.2f} g\n"
            f"Gorduras: {gorduras_totais:.2f} g\n"
            f"Gorduras Saturadas: {gorduras_saturadas:.1f} g"
        )
        
        messagebox.showinfo("Resultado", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = NutritionalCalculatorApp(root)
    root.mainloop()