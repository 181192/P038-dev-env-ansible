import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jetbrains_toolbox(host):
    assert host.run('which jetbrain-toolbox').rc == 0
