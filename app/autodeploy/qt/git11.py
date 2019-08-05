
# -*- coding: utf-8 -*-
import paramiko
import datetime
import os
#创建com目录
def mkdir():
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,username=username,password=password)
        sftp = ssh.open_sftp()

        filename="/data/tomcat_servers/solarman2_api_18003/webapps/ROOT/WEB-INF/classes/com"
        #需要增加一条判断文件是否存在，如果存在不创建，存在就补创建
        sftp.mkdir(filename)
        print "Create folder %s in remote hosts successfully!\n" %filename
        ssh.close()
    except:
        print "Create folder failure!\n"
#递归上传目录里面的文件或者文件夹
def upload(local_dir, remote_dir, hostname, port, username, password):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)

        print('upload file start %s ' % datetime.datetime.now())
        for root, dirs, files in os.walk(local_dir):
            print('[%s][%s][%s]' % (root, dirs, files))
            for filespath in files:
                local_file = os.path.join(root, filespath)
                print(11, '[%s][%s][%s][%s]' % (root, filespath, local_file, local_dir))
                a = local_file.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print('01', a, '[%s]' % remote_dir)
                remote_file = os.path.join(remote_dir, a).replace('\\', '/')
                print(22, remote_file)
                try:
                    sftp.put(local_file, remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                    print("66 upload %s to remote %s" % (local_file, remote_file))
            for name in dirs:
                local_path = os.path.join(root, name)
                print(0, local_path, local_dir)
                a = local_path.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print(1, a)
                print(1, remote_dir)
                # remote_path = os.path.join(remote_dir, a).replace('\\', '/')
                remote_path = remote_dir + a
                print(33, remote_path)
                try:
                    sftp.mkdir(remote_path)
                    print(44, "mkdir path %s" % remote_path)
                except Exception as e:
                    print(55, e)
        print('77,upload file success %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(88, e)
def ssh_clinet(sys_ip,username,password,cmds):
    try:
        #创建ssh客户端
        ssh1 = paramiko.SSHClient()
        #第一次ssh远程时会提示输入yes或者no
        ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #密码方式远程连接
        ssh1.connect(sys_ip, 22, username, password, timeout=20)
        #执行命令
        stdin, stdout, stderr = ssh1.exec_command(cmds[0])
        stdin, stdout, stderr = ssh1.exec_command(cmds[1])
        #获取命令执行结果,返回的数据是一个list
        result = stdout.readlines()
        return result
    except Exception, e:
        print e
    finally:
        ssh1.close()




if __name__ == '__main__':
    # 选择上传到那个服务器
    # serverlist = ['服务器00', '服务器01', '服务器02']
    # for i in range(len(serverlist)):
    #     print ("序号：%s   对应的服务器为：%s" % (i, serverlist[i]))
    # num = raw_input("请输入对应服务器的序号：")
    # num = int(num)
    # hostname = ['10.*.*.*', '10.*.*.*', '10.*.*.*']
    # username = ['root', 'root', 'root']
    # password = ['***', '***', '***']
    # port = [22, 22, 22]
    hostname='192.168.1.58'
    username='root'
    password='123456'
    port=22

    # mkdir()
    local_dir = r'C:\Users\lyy\Desktop\solarman2_api_18003\webapps\ROOT\WEB-INF\classes\com'
    remote_dir = r'/data/tomcat_servers/solarman2_api_18003/webapps/ROOT/WEB-INF/classes/com/'
    cmds=['cd /data/tomcat_servers/','./restart_solarman2_api_18003.sh']
    upload(local_dir, remote_dir, hostname=hostname, port=port, username=username,
           password=password)
    print ssh_clinet(hostname,username,password,cmds)

