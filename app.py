# GitHub    Queuebee2

from flask import Flask, render_template, redirect, request
from complexclass import ComplexClass

""" Disclaimer: geen idee wat wel/niet best-practice is. Dit is mijn beste begrip
    van jinja2 en flask. Graag pullrequests voor veranderingen of toevoegingen!
"""

app = Flask(__name__)

complex_class_obj = ComplexClass()

@app.route('/')
def hello_world():
    # niet conventioneel, maar om te vermijden dat we nu dingen op de homepage doen.
    return redirect('/jeroute')


@app.route('/jeroute', methods=["POST","GET"])
def jeroute():
    """ let op:
    from flask import request, render_template! (jsonify zou ook gebruikt kunnen worden)"""
    # nog geen korte omweg gevonden om variables niet eerst op None/False te zetten
    # anders crasht jinja... om dat te fixen moet je vgm ingewikkelde settings
    # kapot maken van jinja dus dit is de makkelijkste methode
    results = None

    # check of er op dat knoppie gedrukt werd
    if request.method == 'POST':
        if request.form['your_button_name'] == "your_button_value (do something!)":
            print('debug: button was pressed!')

            # hier kun je whatever neerzetten, je eigen method/class.
            # in dit geval is het object een nested dict
            """ # voorbeeld van de data
            {'item 1':{
                'attr1: value1,
                'attr2: value2,
                'attr3: value3 },
             'item 2':{
                'attr1: value4,
                'attr2: value5,
                'attr3: value6 }
             }
            """
            results = complex_class_obj.complex_function()



    # return 'results' object naar de jinja2 template engine
    # als er niet op het knoppie gedrukt is blijft results leeg
    return render_template('je_html.html', results=results)


@app.route('/contact')
def contact_route():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run()
