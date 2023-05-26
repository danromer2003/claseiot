from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "hola a todos "
@app.get("/tortas/{num}")
def tortas(num):
    tortas={
    1"jamon"
      2"milanes"
        3"pollo"
        4"mole"
    }
    return tortas
@app.get("/conversor_caf/{C}")
def temp{C}:
     try:
            C=float(C)
            TF=C*(9/5) + 32
            return f"la temperatura es de {TF} grados sentigrados"
    except:
            return"eso no era"
            
             
            
     
