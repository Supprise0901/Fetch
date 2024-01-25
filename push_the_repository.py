import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified. Pushing changes...')
        self.push_changes()

    def push_changes(self):
        # 推送变更到GitHub
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Auto commit and push'])
        # 配置远程仓库地址
        subprocess.run(['git', 'remote', 'add', 'origin', 'git@github.com:Supprise0901/Fetch.git'])
        # 推送到远程仓库
        subprocess.run(['git', 'push', '-u', 'origin', 'main'])


if __name__ == "__main__":
    # 初始化本地仓库
    subprocess.run(['git', 'init'])
    # 创建文件系统事件处理器
    event_handler = MyHandler()

    # 创建观察者并将事件处理器附加到观察者
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)

    # 启动观察者
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 在键盘中断时停止观察者
        observer.stop()
    observer.join()
