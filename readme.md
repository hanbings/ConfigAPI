# ConfigAPI

> [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) 插件开发用的配置文件管理API

## 依赖的Python模块

- ruamel.yaml

## 使用

```python
from ConfigAPI import Config

def on_load(server, old):
    default = {'key': 'value'}
    global config
    if old is None:
        config = Config('my_plugin_name', default)
    else:
        config = old.config
```

注意: **实例化时需要传递默认配置的dict**

如果同一插件需要多个配置文件, 提供 `config_name` 参数即可

## 方法

| Method | Function |
|- | - |
| config[key] | 支持直接使用 `config[key]` 获取配置项 |
| get(key) | 获取配置项 |
| set(key, value) | 设置配置项的值 |
| reload() | 从文件重载配置 |
| reset_default() | 将所有配置恢复为默认配置 |
| get_default(key) | 获取一项配置的默认值 |

调用 `get` 时如果无法找到配置项会抛出 `ValueError` 异常, 提示 `key` 不在配置中

调用 `set` 和 `set_default` 时如果配置项不在默认配置内会抛出 `ValueError` 异常, 提示 `key` 未注册
