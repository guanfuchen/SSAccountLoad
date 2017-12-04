sudo netstat -tlnp | awk '/:1082 */ {split($NF,a,"/"); print a[1]}'
