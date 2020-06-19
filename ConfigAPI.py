# -*- coding: utf-8 -*-
import configparser
import os


def on_load(server, old_module):
    # Logo
    print("\033[34m")
    print("""
    [ConfigAPI] ConfigAPI Hanbings 3219065882@qq.com
    
    _________                _____.__          _____ __________.___          
    \\_   ___ \\  ____   _____/ ____\\__| ____   /  _  \\\\______   \\   |   
    /    \\  \\/ /  _ \\ /    \\   __\\|  |/ ___\\ /  /_\\  \\|     ___/   | 
    \\     \\___(  <_> )   |  \\  |  |  / /_/  >    |    \\    |   |   |     
     \\______  /\\____/|___|  /__|  |__\\___  /\\____|__  /____|   |___|     
            \\/            \\/        /_____/         \\/                    
    """)
    print("\033[0m")
    server.logger.info('[ConfigAPI] ConfigAPI 已被加载')
    # 作者声明
    server.add_help_message('§l[ConfigAPI]', ' §6ConfigAPI Hanbings 3219065882@qq.com')


# 创建新的配置文件
def new_config(config_name):
    f = open('config/' + config_name, 'w')
    f.close()


# 创建自定义目录文件
def new_file(path):
    f = open(path, 'w')
    f.close()


# 检查（指定）配置文件是否已经存在
def has_config(config_name):
    if not os.path.isfile("config/" + config_name):
        return False


# 检查文件是否已经存在
def has_file(path):
    if not os.path.isfile(path):
        return False


# 检查ini配置文件[section]是否存在
def has_ini_config_section(config_name, section):
    config = configparser.ConfigParser()
    config.read('config/' + config_name)
    if not config.has_section(section):
        return False
    else:
        return True


# 检查ini配置文件[option]是否存在
def has_ini_config_option(config_name, section, option):
    config = configparser.ConfigParser()
    config.read('config/' + config_name)
    if not config.has_option(section, option):
        return False
    else:
        return True


# 检查ini配置文件[option]是否存在
def has_ini_file_option(path, section, option):
    config = configparser.ConfigParser()
    config.read(path)
    if not config.has_option(section, option):
        return False
    else:
        return True


# 检查自定义目录的ini文件[section]是否存在
def has_ini_file_section(path, section):
    config = configparser.ConfigParser()
    config.read(path)
    if not config.has_section(section):
        return False
    else:
        return True


# 读取ini配置文件指定[section]的[value]
def get_ini_config_value(config_name, section, option):
    config = configparser.ConfigParser()
    config.read("config/" + config_name)
    return config.get(section, option)


# 读取指定目录ini配置文件[section]的[value]
def get_ini_file_value(path, section, option):
    config = configparser.ConfigParser()
    config.read(path)
    return config.get(section, option)


# 设置ini配置文件的[section]
def set_ini_config_section(config_name, section):
    f = open('config/' + config_name, 'w')
    config = configparser.ConfigParser()
    config.add_section(section)
    config.write(f)
    f.close()


# 设置ini配置文件的[value]
def set_ini_config_value(config_name, section, option, value):
    f = open('config/' + config_name, 'w')
    config = configparser.ConfigParser()
    config.set(section, option, value)
    config.write(f)
    f.close()


# 设置指定目录ini配置文件的[section]
def add_ini_file_section(path, section):
    f = open(path, 'w')
    config = configparser.ConfigParser()
    config.add_section(section)
    config.write(f)
    f.close()


# 设置指定目录ini配置文件的[value]
def set_ini_file_value(path, section, option, value):
    f = open(path, 'w')
    config = configparser.ConfigParser()
    config.set(section, option, value)
    config.write(f)
    f.close()
