from invoke import task


@task
def init(ctx, force_reinstall=False):
    """Check pre-requirements"""
    cmd = "pip install -r requirements.txt"
    if force_reinstall:
        cmd + " --force-reinstall"
    ctx.run(cmd, pty=True)


@task(help={
    'debug': 'append -vvvv debug flag on ansible-controller',
    'tags': 'a list of playbook tags to run'
})
def run(ctx, debug=False, tags=[]):
    """Run ansible playbook"""
    cmd = "ansible-playbook main.yaml"
    if debug:
        cmd += " -vvvv"
    if tags:
        cmd += " --tags "
        for tag in tags:
            cmd += tag
    ctx.run(cmd, pty=True)
