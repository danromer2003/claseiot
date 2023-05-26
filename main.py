from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "hola a todos amigos"
@app.get("/pizza/{num}")
def pizzas(num):
    pizzas={
     1"hawaiana"
      2"pepperoni"
        3"queso"
        4"pollo"
    }
    return pizzas
@app.get("/conversor_caf/{C}")
def temp{C}:
     try:
            C=float(C)
            TF=C*(9/5) + 32
            return f"la temperatura es de {TF} grados sentigrados"
    except:
            return"eso no era"
