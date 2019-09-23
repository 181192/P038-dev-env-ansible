# Development Environment with Ansible

## Requirements

```
sudo apt-get install gcc python3-dev

git clone https://github.com/181192/P038-dev-env-ansible
cd P038-dev-env-ansible

./setup-direnv.sh
direnv allow

pip install -r requirements.txt
```

## Install / setup

```
ansible-playbook main.yaml --ask-become-pass

# With debug (-v -vv -vvv -vvvv)
ansible-playbook main.yaml --ask-become-pass -vvvv
```

Install with tags:
```
ansible-playbook main.yaml --tags "utilities,code" --ask-become-pass -vvvv

ansible-playbook main.yaml --tags utilities --ask-become-pass -vvvv

ansible-playbook main.yaml --skip-tags "code" --ask-become-pass -vvvv
```

## Testing

[Molecule](https://molecule.readthedocs.io/en/stable/) is used for E2E testing.

```
pip install molecule
```

To run E2E test go to `roles/<role>` and run:

```
molecule test
```

## Developing

To add a new role go to the `roles` and run

```
molecule init role -r my-new-role
```


### OS flags

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