import sys
import time
import subprocess

def read_config(path):
    """读取文件，返回执行频率和Python路径"""
    with open(path, 'r') as f:
        try:
            lines = f.readlines()
            frequency = int(lines[0].replace('#', '').replace(' ', '').strip())
            frequency = frequency / 60
            py_path = lines[1].replace('#', '').replace(' ', '').strip()
        except (IndexError, ValueError):
            print("配置文件格式错误")
            return None, None
    return frequency, py_path

def job(path, py_path='python'):
    """执行指定的 Python 脚本"""
    subprocess.call([py_path, path])

def run():
    """主函数"""
    if len(sys.argv) != 2:
        print("Usage: mmr <mathmodel_file>")
        sys.exit(1)

    path = sys.argv[1]
    frequency, py_path = read_config(path)

    if frequency is None:
        return

    while True:
        job(path, py_path)
        time.sleep(frequency)

if __name__ == '__main__':
    run()
