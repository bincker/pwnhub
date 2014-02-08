import requests
import json
import base64
endpoint = 'https://api.github.com/search/code?q='
headers = {'Accept': 'application/vnd.github.preview', 'Content-Type':'application/json'}




def search_code(search,repo):
    potential_vulns = []
    r = requests.get(endpoint + search+"+repo:" + repo , auth=('henryhoggard', 'password'), headers=headers)
    results = json.loads(r.text)
    if results['total_count'] != 0:
        for result in results['items']:
            print result['url']
            r = requests.get(result['url'], headers=headers)
            code_result = json.loads(r.text)
            code = code_result['content']
            code.replace('\n', '')
            code = base64.b64decode(code)
            potential_vulns.append(code)
            print code
            

    return potential_vulns


def php_sqli_checks(code):
    if ("mysql_real_escape_string" in code or "int(" in code or "prepare(" in code)  :
        return False
    else:
        return True


def php_xss_checks(code):
    if ("escapestring") in code or "htmlspecialchars" in code:
        print "lol"



php_sql_vulns = {"mysql_query", "where ", "select ", "insert "}
php_rce_vulns = {"system(", "exec(", "shell_exec("}
php_rfi_vulns = {"require(", "include(", "require_once(", "include_once("}
php_object_injection_vulns = {"unserialize("}
php_xss_vulns = {"echo("}
php_requests = {"$_GET","$_POST", "$_REQUEST", "$_COOKIE"}

android_vulns = {""}


for req in php_requests:
    for vuln in php_object_injection_vulns:
        search_code(vuln + " " + req, "mybb/mybb")
