class ssh {
  file {
    '~/.ssh/school'
    ensure  => 'present',
    owner   => 'user',
    group   => 'user',
    mode    => '0600',
    content => template('ssh/config.erb'),
  }
}
