#bash script create key RSA

include stdlib
file { '/etc/.ssh/config':
  ensure  => file,
  owner   => 'your_username',
  group   => 'your_username_group',
  mode    => '0600',
  content => "
Host *
    PasswordAuthentication no

Host your_server_hostname
    IdentityFile ~/.ssh/school
",
}

