cd /var/www/html/testApi
python manage.py dbshell <<EOF
update testapp_info set lastcommitsha="$1";
EOF
