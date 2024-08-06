# What did you learn
## 1. os moudle
    __file__
    os.path.listdir(`dir`)
    os.path.join(`dir`, `filename`)
    os.path.abspath(__file__)
    os.path.dirname(__file__)
    os.path.basename(`file`)
    os.path.splitext(`filename`)
    os.path.expanduser('~')
    os.path.getmtime(`file_path`)
    os.path.exists(`path`)
    os.rename(`file1`, `file2`)
    os.getcwd()
    os.makedirs()
    os.remove(`file`)

## 2. argparse
    def get_args():
        parse = argparse.ArgumentParser(
            description="Here is the description of the script"
        )
        parse.add_argument(
            "arg_name", type=str, nargs=1, metavar="ARG", help="Here is the description of this arguemnt"
        )
        return vars(parse.parse_args())                 # vars(): Get the attributes and attribute values of an object

    def main():
        args = get _args()                              # dictionary
        print(f"args: {args["arg_name"][0]}")           # usage

## 3. tkinter
[tkinter_example](https://github.com/WuLyon/PythonCode/blob/main/Lession3_youtube/set_max_velocity.py)

## 4. from threading import Thread
    def threading():
        # Call work function
        `thread_name` = Thread(target=`func_name`)
        `theread_name`.start()
    
## 5. from PIL import Image, ImageDraw, ImageFont
    pip install Pillow
    image_obj = Image.open(`the path to image.jpg`)
    draw_obj = ImageDraw.Draw(image)
    font_obj = ImageFont.turetype(`the path to font.ttf`, size=`int`)  
    # C:\Windows\Fonts covers all the system fonts could be useful
    draw_obj.text(`position`, `text`, font=`font_obj`, fill=`color`)
    image_obj.save(`path`, `type`)   # "jpg" must be "jpeg"

## 6. subprocess
    subprocessCompleted_obj = subprocess.run(
            `command`,                          # Should be in the format like: ['ls', '-a']   
            shell=True,                         # Could make `command` using string directly
            check=True,                         # Check if the returncode is 0. if not, raise an error
            stdout=subprocess.PIPE,             # capture the output with the format of byte
            stderr=subprocess.PIPE,             # capture the error with the format of byte
            universal_newlines=True)            # Change the output and error from byte format into string format

    # To get the output, you need to:
    vars(subprocessCompleted_obj)['stdout']

    # To get the error, you need to:
    vars(subprocessCompleted_obj)['stderr']

    # For simple usage:
    output = subprocess.check_output(`command`, shell=True, universal_newlines=True)

More info:

[RUNOOB.com](https://www.runoob.com/w3cnote/python3-subprocess.html)

[csdn.net](https://blog.csdn.net/qq_43331089/article/details/124421661)

## 7. random
    random.shuffle(`list`)                      # Reverse the order of the elements in the list

## 8. file
    with open('file.txt', 'r') as file:
        `context` = file.read()                   

    with open('file.txt', 'w') as file:
        file.write(`context`)
    
    file.read()                                 # string
    file.readlines()                            # list, element with '\n'
    context.splitlines()                        # list, element is each line of context without '\n'

## 9. string
    str.strip(), str.lstrip(), str.rstrip()     # remove spaces of string
    str = '`character`'.join(`string`)

## 10. list
    list.append(`element`)
    list.insert(`index`, `element`)
    list.remove(`element`)                      # The first matching element
    list.pop()                                  # The last element
    del list[`index`]
    list.clear()
    list.index(`element`)                       # The first matching element
    list.count(`element`)
    list.sort()                                 # Modify the original list
    list.sort(reverse=True)
    sorted(`list`)                              # Generate a new list
    sorted(`list`, reverse=True)
    list.reverse()
    list.copy()
    len(`list`)
    list = [x ** 2 for x in range(6)]

## 11. git commmand
    # 初始化和配置
    git init                  # 初始化一个新的 Git 仓库
    git clone <repo-url>      # 克隆一个远程仓库
    git config --global user.name "Your Name"    # 设置全局用户名
    git config --global user.email "your.email@example.com"  # 设置全局用户邮箱

    # 状态和日志
    git status                # 查看工作目录状态
    git status -sb            # 查看当前分支跟踪的远程分支
    git log                   # 查看提交历史
    git log --oneline         # 简洁地查看提交历史

    # 添加和提交
    git add <file>            # 添加指定文件到暂存区
    git add .                 # 添加所有文件到暂存区
    git commit -m "Commit message"   # 提交暂存区的内容

    # 分支管理
    git branch                # 列出所有本地分支
    git branch -a             # 列出所有分支（包括远程分支）
    git branch -vv            # 查看所有本地分支跟踪的远程分支
    git branch --set-upstream-to=<remote-branch>    # 将本地分支设置为跟踪远程分支
    git branch <branch-name>  # 创建新分支
    git branch -d <branch-name> # 删除指定分支
    git branch -D <branch-name> # 强制删除指定分支
    git checkout <branch-name>  # 切换到指定分支
    git checkout -b <branch-name>  # 创建并切换到新分支
    git merge <branch-name>   # 合并指定分支到当前分支

    # 远程操作
    git remote -v             # 查看远程仓库
    git remote add <name> <url>  # 添加远程仓库
    git remote remove <name>  # 移除远程仓库

    # 获取和推送
    git fetch                 # 从远程仓库获取更新
    git pull                  # 获取并合并远程分支的更新
    git push                  # 推送本地分支到远程仓库
    git push --set-upstream origin <branch-name>  # 将本地分支设置为跟踪远程分支并推送
    git push origin --delete <branch-name>  # 删除远程分支

    # 撤销和重置
    git restore <file>        # 移除未暂存的更改
    git reset <file>          # 从暂存区移除指定文件
    git reset --hard          # 重置工作目录和暂存区
    git reset --hard <commit> # 重置到指定提交
    git reset --hard <remote-branch> #重置到指定的远程分支
    git revert <commit>       # 撤销指定提交

    # 查看差异
    git diff                  # 查看未暂存的更改
    git diff --cached         # 查看已暂存的更改
    git diff <branch1> <branch2>  # 比较两个分支之间的差异

    # 清理
    git clean -f              # 删除未跟踪的文件
    git clean -fd             # 删除未跟踪的文件和目录

## 12. glob moudle
    zip_files = glob.glob(os.path.join(directory, "*.zip"))

## 13. time moudle
    time.time() # 当前时间自纪元(1970/1/1)的秒数
    time.ctime(`time`) # 转换为可读的时间

## Tips:
    -There are 3 way to type the path in Windows:
        r"C:\Path\to\the\file.ext"
        "C:\\path\\to\\the\\file.ext"
        "C:/path/to/the/fiile.ext"


