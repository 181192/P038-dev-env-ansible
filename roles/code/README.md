Ansible Role: Visual Studio Code
=========

Role to install the [Visual Studio Code](https://code.visualstudio.com) IDE / text editor.

Requirements
------------

[Molecule](https://molecule.readthedocs.io/en/stable/) is used for E2E testing.

```
pip install molecule
```

To run E2E test go to `roles/<role>` and run:

```
molecule test
```

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Visual Studio Code version number (defaults to the latest version)
visual_studio_code_version: ''

# Build (either 'stable' or 'insiders') https://code.visualstudio.com/insiders/
# Ubuntu only (code-insiders isn't in Microsoft's RPM repo)
visual_studio_code_build: stable

```

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: code
```

Playbook with extensions installed:

```yaml
- role: code
  visual_studio_code_extensions:
    - ms-python.python
    - wholroyd.jinja
  visual_studio_code_settings: {
    "editor.rulers": [80, 100, 120],
    "editor.renderWhitespace": true,
    "files.associations": {
      "Vagrantfile": "ruby"
    }
  }
```

