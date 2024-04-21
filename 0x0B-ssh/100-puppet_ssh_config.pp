#!/usr/bin/env bash
#bash script create key RSA

file { '/home/your_username/.ssh/config':
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

