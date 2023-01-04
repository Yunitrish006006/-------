#!/bin/bash
chown -R www-data ../html
chgrp -R www-data ../html
chmod -R 777 ../html

chown root permit.sh
chgrp root permit.sh

chown root database
chgrp root database
chmod -R 777 database