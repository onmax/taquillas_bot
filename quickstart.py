from __future__ import print_function
import httplib2
import os
import time
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
from telebot import types
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def imprimirDatos(values, contPG):
    if(contPG != 0):
        maximo = contPG * 50
        minimo = (contPG-1) * 50


    final_text = ""
    for arr in values:
        if('maximo' not in locals() or contPG != 0 and contPG> minimo and contPG <= maximo):
            if(len(arr[0])==0):
                arr_nombres = "NONE"
            else:
                arr_nombres = arr[0]
            if (len(arr[1]) == 0):
                arr_apellidos = "NONE"
            else:
                arr_apellidos = arr[1]
            if (arr[2] != 0):
                arr_matricula = "NONE"
            else:
                arr_matricula = arr[2]
            final_text += "<b>" + str(contPG) + "</b>- " + arr_apellidos + ", " + arr_nombres + " (" + arr_matricula + ")\n"
            contPG += 1
        else:
            contPG += 1
    if(len(final_text) == 0):
        return "No se ha encontrado ningún dato"
    else:
        return final_text

def todos(contPG):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1wdXri_xe4rOTBtCHJcA3r7_43L6aaecfTzCw6qCxtq8'
    rangeName = 'B2:D1000'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        return 'No se ha encontrado ningun dato.'
    else:
        values = sorted(values, key=lambda values: values[1])
        return imprimirDatos(values, contPG)


def buscar_matricula(num_matricula, time):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1wdXri_xe4rOTBtCHJcA3r7_43L6aaecfTzCw6qCxtq8'
    rangeName = 'B2:D1000'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        return 'No se ha encontrado ningún dato.'
    else:
        resultado = "No se ha encontrado nada."
        num_matricula = num_matricula.replace("y", "")
        limite = 0
        for i in values:
            if len(i) == 3 and num_matricula in i[2] and limite < 75:
                i[2] = i[2].replace("y", "")
                if limite == 0:
                    resultado = ""
                resultado += "<b>y" + num_matricula + ": </b>" + i[1] + ", " + i[0]+ "\n"
                limite += 1
        print(time + ": " + resultado.replace("<b>", "").replace("</b>", "").replace(":", " -"))
        return resultado



def buscar_nombre(nombre, time):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1wdXri_xe4rOTBtCHJcA3r7_43L6aaecfTzCw6qCxtq8'
    rangeName = 'B2:D1000'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        return 'No se ha encontrado ningún dato.'
    else:
        resultado="No se ha encontrado nada."
        limite=0
        minus = nombre.lower()
        for i in values:
            i[0] = i[0].lower()
            if minus in i[0] and limite < 75:
                if limite == 0:
                    resultado = ""
                limite += 1
                resultado += str(limite) + "- <b>" + i[0] + " </b>" + i[1] + ", " + i[2]+ "\n"
        print(time + ": " + resultado.replace("<b>", "").replace("</b>", ""))
        return resultado

if __name__ == '__main__':
    main()
