#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""
from fabric.api import *
import os.path
from fabric.operations import run, put, sudo
from datetime import datetime
env.hosts = ['35.196.149.169', '35.185.80.112']
env.user = 'ubuntu'


def do_pack():
    """  return the archive path if the archive has correctly generated """
    try:
        archive = datetime.now().strftime("%Y%m%d%H%M%S")
        local("sudo mkdir -p versions")
        val = local("tar -cvzf versions/web_static_{}.tgz web_static/".
                    format(archive))
        res = "versions/web_static_{:s}.tgz".format(archive)
        return res

    except BaseException:
        return None

def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    tmp_path = "/tmp/{}".format(file_name)
    no, wout = os.path.splitext(file_name)
    dest = "/data/web_static/releases/{}".format(no)
    curr = "/data/web_static/current"
    try:
        put(archive_path, tmp_path)
        run("sudo mkdir -p {}".format(dest))
        run("sudo tar -xzf {} -C {}".format(tmp_path, dest))
        run("sudo rm {}".format(tmp_path))
        run("sudo mv {}/web_static/* {}/".format(dest, dest))
        run("sudo rm -rf {}/web_static".format(dest))
        run("sudo rm -rf {}".format(curr))
        run("sudo ln -s {} {}".format(dest, curr))
        return True
    except:
        return False

def deploy():
    """ return value of do_deploy """
    path = do_pack.do_pack()
    try:
        return do_deploy(path)
    except BaseException:
        return False
