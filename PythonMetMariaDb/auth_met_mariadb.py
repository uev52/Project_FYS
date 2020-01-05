
import mysql.connector as mariadb
import urllib.parse as urlparse
import subprocess


def application(environ, start_response):

    mariadb_connection = mariadb.connect(user='groep2', password='humam123', database='corendon')
    cursor = mariadb_connection.cursor()


    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)
    html = ''
    #html += '<html>\n'
    #html += ' <body>\n'
    #html += ' <title>Test WSGI page for fys</title>\n'
    #html += ' <div style="width: 100%; font-size: 20px; font-weight: bold; text-align: center;">\n'
    #html += ' Welcome to the mod_wsgi test page\n'
    #html += ' </div>\n'
    #html += ' <h2>Some interesting environment variables:</h2>\n'
    #html += ' <div style="width: 100%; font-family: Courier; font-size: 14px; font-weight: bold; text-align: left;">\n'
    #html += ' <h2>Request parameters</h2>\n'
    #html += ' <div style="width: 100%; font-family: Courier; font-size: 14px; font-weight: bold; text-align: left;">\n'
    # check HTTP request method and get parameters from request
    method = environ.get('REQUEST_METHOD', '')
    params = {}

    if method == 'GET':
        params = urlparse.parse_qs(environ['QUERY_STRING'])
    elif method == 'POST':
        input = environ['wsgi.input'].read().decode()
        params = urlparse.parse_qs(input)

    html += 'Userid: ' + params.get('userid', [''])[0] + '<br>\n'
    html += 'Password: ' + params.get('password', [''])[0] + '<br>\n'

    environmentVars = ['REQUEST_METHOD', 'REQUEST_URI', 'QUERY_STRING', 'SCRIPT_NAME', 'HTTP_REFERER', 'REMOTE_ADDR']
    for envVar in environmentVars:
        envVarValue = environ.get(envVar, '')
        html += envVar + ' = ' + envVarValue + '<br>\n'

    realIP = environ.get('REMOTE_ADDR', '')
    ipuser = str(realIP)
    coruser = params.get('coruser', [''])[0]
    corpassword = params.get('corpassword', [''])[0]
    notaccept = ['like', 'select', 'or', 'where', 'from', 'corendon', 'drop', 'commit', 'update', 'rollback', "script"]

    coruser = coruser.lower()
    cursor.execute("select count(*) from passenger where lastName=%s AND ticketNumber=%s", (coruser, corpassword))
    result = cursor.fetchone()

    if result[0] != 0 and coruser.isalpha() and coruser not in notaccept:
        start_response('301 Moved Permanently', [('Location', 'https://192.168.4.1/welkomstpagina_Corendon.html')])
        subprocess.call(["sudo", "iptables", "-t", "nat", "-I", "PREROUTING", "-s", ipuser, "-j", "ACCEPT"])
    else:
        start_response('301 Moved Permanently', [('Location', 'https://192.168.4.1')])

    return [bytes("1", 'utf-8')]

