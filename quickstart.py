from __future__ import print_function
import httplib2
import os

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
            arr_nombres = arr[0]
            arr_apellidos = arr[1]
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






def buscar_matricula(num_matricula):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1wdXri_xe4rOTBtCHJcA3r7_43L6aaecfTzCw6qCxtq8'
    rangeName = 'D2:D1000'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        return 'No se ha encontrado ningún dato.'
    else:
        cont = 2
        for i in values:
            if (i[0] == num_matricula):
                rangeName = 'B' + str(cont) + ':D' + str(cont)
                result = service.spreadsheets().values().get(
                    spreadsheetId=spreadsheetId, range=rangeName).execute()
                values = result.get('values', [])
                contPG = 1
                return imprimirDatos(values, contPG)
            else:
                cont += 1

def buscar_nombre(nombre_a_buscar):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1wdXri_xe4rOTBtCHJcA3r7_43L6aaecfTzCw6qCxtq8'
    rangeName = 'B2:B1000'

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        return 'No se ha encontrado ningún dato.'
    else:

        cont = 2
        resultado = ""
        for i in values:
            print(i)
            if (i[0] == nombre_a_buscar):
                rangeName = 'B' + str(cont) + ':D' + str(cont)
                result = service.spreadsheets().values().get(
                    spreadsheetId=spreadsheetId, range=rangeName).execute()
                values = result.get('values', [])

                resultado = imprimirDatos(values, 0) + "\n"
            else:
                cont += 1

    return resultado

if __name__ == '__main__':
    main()
