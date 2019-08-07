# Development Environment with Ansible




RHEL/CentOS
```
when: ansible_distribution == 'CentOS' or ansible_distribution == 'Red Hat
Enterprise Linux'
```

DEBIAN/Ubuntu
```
when: ansible_distribution == 'Debian' or ansible_distribution == 'Ubuntu'
```


```
when: ansible_os_family == "CentOS"
when: ansible_os_family == "Redhat"
when: ansible_os_family == "Darwin"
when: ansible_os_family == "Debian"
when: ansible_os_family == "Windows"
```


```
OS_FAMILY = dict(
    RedHat = 'RedHat',
    Fedora = 'RedHat',
    CentOS = 'RedHat',
    Scientific = 'RedHat',
    SLC = 'RedHat',
    Ascendos = 'RedHat',
    CloudLinux = 'RedHat',
    PSBM = 'RedHat',
    OracleLinux = 'RedHat',
    OVS = 'RedHat',
    OEL = 'RedHat',
    Amazon = 'RedHat',
    XenServer = 'RedHat',
    Ubuntu = 'Debian',
    Debian = 'Debian',
    SLES = 'Suse',
    SLED = 'Suse',
    OpenSuSE = 'Suse',
    SuSE = 'Suse',
    Gentoo = 'Gentoo',
    Archlinux = 'Archlinux',
    Mandriva = 'Mandrake',
    Mandrake = 'Mandrake',
    Solaris = 'Solaris',
    Nexenta = 'Solaris',
    OmniOS = 'Solaris',
    OpenIndiana = 'Solaris',
    SmartOS = 'Solaris',
    AIX = 'AIX',
    Alpine = 'Alpine',
    MacOSX = 'Darwin',
    FreeBSD = 'FreeBSD',
    HPUX = 'HP-UX'
)
```