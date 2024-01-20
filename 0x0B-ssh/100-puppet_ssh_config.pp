# set up my client SSH configuration

exec { 'config SSH client':
  command => "echo -e 'IdentityFile ~/.ssh/school\nPasswordAuthentication no\n' >> /etc/ssh/ssh_config",
  path    => '/bin:/usr/bin',
}
