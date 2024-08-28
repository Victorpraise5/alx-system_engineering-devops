# Enable holberton user to open a file without any error message.
exec { 'file_limit':
  command  => "sed -i -e '/holberton hard/s/.$/8192/' -e '/holberton soft/s/.$/2048/' /etc/security/limits.conf",
  provider => 'shell'
}
