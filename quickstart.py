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

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    "
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

def imprimirDatos(values):
    cont = 1
    final_text = ""
    for arr in values:
        arr_nombres = arr[0]
        arr_apellidos = arr[1]
        arr_matricula = arr[2]
        arr_fechaCaducidad = arr[3]
        final_text += str(
            cont) + "- " + arr_apellidos + ", " + arr_nombres + "(" + arr_matricula + "): " + arr_fechaCaducidad + "\n"
        cont += 1
    return final_text

def todos():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1wdXri_xe4rOTBtCHJcA3r7_43L6aaecfTzCw6qCxtq8'
    rangeName = 'B2:E1000'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        return 'No se ha encontrado ningun dato.'
    else:
        return imprimirDatos(values)

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
                rangeName = 'B' + str(cont) + ':E' + str(cont)
                result = service.spreadsheets().values().get(
                    spreadsheetId=spreadsheetId, range=rangeName).execute()
                values = result.get('values', [])
                return imprimirDatos(values)
            else:
                cont += 1


    return "No se ha encontrado ninguna matrícula :/"
if __name__ == '__main__':
    main()
