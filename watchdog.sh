#!/bin/bash
# Test for network conection
for interface in $(ls /sys/class/net/ | grep -v lo);
do
  if [[ $(cat /sys/class/net/$interface/carrier) = 1 ]]; then OnLine=1;
          STATUS="$(systemctl is-active pwm-led.service)"
          if [ "${STATUS}" = "active" ]; then
                  echo "Service Fan Hat is running..."
          else
                  echo " Service Fan Hat is not running.... so exiting "
                  systemctl restart pwm-led.service;
          fi
  fi
done
if ! [ $OnLine ]; then echo "Not Online" > /dev/stderr;
        systemctl stop pwm-led.service;
        systemctl start pwm-led.service;
        exit;
fi
