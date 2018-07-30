#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""
do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')


def deploy():
    """ return value of do_deploy """
    path = do_pack.do_pack()
    try:
        return do_deploy.do_deploy(path)
    except BaseException:
        return False
