# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd
app = Flask(__name__)
df = pd.read_excel("Base.xlsx")

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if ('Ayuda' in incoming_msg) or ('ayuda' in incoming_msg):
        # return a quote
        quote = 'Para poder identificar si su producto es verdadero, para ello necesito que escribas # y el codigo del producto, por ejemplo #AAAA00000. '
        msg.body(quote)
        responded = True

    if ('Hola' in incoming_msg) or   ('hola' in incoming_msg)  :
        # return a quote
        quote = 'Hola, soy el asistente de Honda y te ayudare a validar la autenticidad de nuestros productos.' \
                'Para ello necesito que escribas # y el codigo del producto, por ejemplo #AAAA00000.'
        msg.body(quote)
        responded = True

    if '#' in incoming_msg:
        # return a cat pic
        incoming_msg = incoming_msg.replace("#","").replace("-","").upper()
        largo = len(incoming_msg)
        print(incoming_msg)
        print(largo)
        if largo== 12:
            valor = df["Codigo2"].isin([incoming_msg]).sum()
            print(valor)
            if valor >0:
                msg.body("Producto Original Validado")
            else:
                msg.body("Producto No Registrado")
        else:
            msg.body("Por favor intentelo de nuevo el codigo del producto de manera correcta debe contener 12 caracteres!")
        responded = True

    if not responded:
        msg.body('Por favor, escriba "Ayuda" y lo apoyare brindadoles las instrucciones de mis funciones!')
    return str(resp)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
