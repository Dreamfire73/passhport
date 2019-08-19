Add a WSGI server in front of PaSSHport
=======================================

PaSSHport is based on Flask, the builtin web server can handle only one request at a time. It means that you can't really use it in production environnement...

In order to handle more requests, we duplicate the PaSSHport process for every connection. Apache provides such a solution with WSGI... And it's quite easy to activate it.

Installation
------------

On Debian :

.. code-block:: none

    apt install apache2 libapache2-mod-wsgi-py3
 
Configuration
-------------

Create a new apache vhost file with this content:

.. code-block:: none

    Listen 5000
    <VirtualHost *:5000>
        ServerName passhport
        
        SSLEngine               on
        SSLCertificateFile      /home/passhport/certs/cert.pem
        SSLCertificatekeyFile   /home/passhport/certs/key.pem
        
        WSGIDaemonProcess passhport user=passhport group=passhport threads=5
        WSGIScriptAlias / /home/passhport/passhport/tools/passhportd.wsgi
        <Directory /home/passhport/ >
            WSGIProcessGroup passhport
            WSGIApplicationGroup %{GLOBAL}
            # passhportd don't provides authentication, please filter by IP
            Require ip 127.0.0.1/8 ::1/128        
        </Directory>
    </VirtualHost>

Activate
--------
First kill the current passhport process

.. code-block:: none

    pkill passhportd

Deactivate default website and activate this one:

.. code-block:: none

    a2dissite 000-default
    a2enmod ssl
    a2ensite passhport.conf
    
    systemctl restart apache2

and Voilà.
