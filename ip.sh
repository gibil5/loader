
#THEIP=$(ifconfig | grep 'inet addr:'| grep -v '127.0.0.1' | tail -1 | cut -d: -f2 | awk '{ print $1}')

#PS1="\[\033[01;31m\]\u@"$THEIP" \w $\[\033[00m\] ";

#THEIP2=$(hostname -i)

PS12=$(ifconfig $(route -n | grep ^0.0.0.0 | awk '{print $NF}') | grep inet | grep -v inet6 | awk '{print $2}')


#echo $THEIP
#echo $THEIP2
#echo $PS1
echo $PS12

