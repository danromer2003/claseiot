from fastapi import FastAPI



app=FastAPI()


@app.get("/")
def index(): 
        return "Hola a todos, quieres saber de spider man nenes"

@app.get("/Spider/{num}")
def spi(num):
        spi={
        "1":"peter parker",
        "2":"mary jane",
        "3": "venom",
        "4": "arena"
        
        }
        
        return spi 

@app.get("/Conversor_CaF/{C}")
def conversorCaf(C):
       try: 
                C=float(C)
                TF=C*(9/5) + 32
                return f"La temperatura es de {TF} grados farenheit"
       except: 
                return "Entrada invalida"
                
@app.get("/RevisarEdad/{E1}/{E2}")
def revisar_edades(E1,E2):
        E1=int(E1)
        E2=int(E2)
        if E1>E2+30:
                return "Podrias ser su Abuelo"
        elif E1>E2+15:
                return "Podrias ser su padre"
        elif E1>E2:
                return "eres mayor"
        elif E2>E1+30:
                return "podria ser tu abuelo"
        elif E2>E1+15:
                return "Podria ser tu padre"
        elif E2>E1:
                return "Es mayor que tu"
        else:
                return "tienen la misma edad"

