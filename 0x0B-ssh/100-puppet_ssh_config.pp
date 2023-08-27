# Using puppet, create a file with below specifications

file { 'configuration file':
    path => '/etc/ssh/ssh_config',
    ensure  => file,
    content => 'Host 54.210.173.28
                  PasswordAuthentication no
                  IdentityFile ~/.ssh/school'
}
