# Using puppet, create a file with below specifications

file { 'ssh':
    ensure  => file,
    content => 'Host 54.210.173.28
                  PasswordAuthentication no
                  IdentityFile ~/.ssh/school'
}
