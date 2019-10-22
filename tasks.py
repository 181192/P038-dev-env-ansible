from invoke import task


@task
def init(ctx, force_reinstall=False):
    """Check pre-requirements"""
    ctx.run("bash workaround-python3-apt.sh", pty=True)

    cmd = "pip install -r requirements.txt"
    if force_reinstall:
        cmd + " --force-reinstall"
    ctx.run(cmd, pty=True)


@task(help={
    'debug': 'append -vvvv debug flag on ansible-controller',
    'ask-become-pass': 'ask for privilege escalation password',
    'tags': 'a list of playbook tags to run'
})
def run(ctx, debug=False, ask_become_pass=True, tags=[]):
    """Run ansible playbook"""
    cmd = "ansible-playbook main.yml"
    if ask_become_pass:
        cmd += " --ask-become-pass"
    if debug:
        cmd += " -vvvv"
    if tags:
        cmd += " --tags "
        for tag in tags:
            cmd += tag
    ctx.run(cmd, pty=True)
