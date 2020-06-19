# ConfigAPI

### MCDR快速创建配置文件API



### Install / 安装它

将它放至MCDR的plugins目录下 （而不是单独运行）

MCDR：https://github.com/Fallen-Breath/MCDReforged/



### Use / 使用它

| 方法名                                                    | 功能                                      | 示例                             |
| --------------------------------------------------------- | ----------------------------------------- | -------------------------------- |
| new_config(config_name)                                   | 在config目录创建新的配置文件              | new_config(”ConfigAPI.ini“)      |
| new_file(path)                                            | 创建自定义目录文件                        | new_file(”config/ConfigAPI.ini”) |
| has_config(config_name)                                   | 检查（指定）配置文件是否已经存在          | has_config(”ConfigAPI.ini”)      |
| has_file(path)                                            | 检查文件是否已经存在                      | has_file(”config/ConfigAPI.ini”) |
| has_ini_config_section(config_name, section)              | 检查ini配置文件[section]是否存在          | -                                |
| has_ini_file_section(path, section)                       | 检查自定义目录的ini文件[section]是否存在  | -                                |
| get_ini_config_value(config_name, section, option)        | 读取ini配置文件指定[section]的[value]     | -                                |
| get_ini_file_value(path, section, option)                 | 读取指定目录ini配置文件[section]的[value] | -                                |
| add_ini_config_section(config_name, section)              | 设置ini配置文件的[section]                | -                                |
| set_ini_config_value(config_name, section, option, value) | 设置ini配置文件的[value]                  | -                                |
| add_ini_file_section(path, section)                       | 设置指定目录ini配置文件的[section]        | -                                |
| set_ini_file_value(path, section, option, value)          | 设置指定目录ini配置文件的[value]          | -                                |

