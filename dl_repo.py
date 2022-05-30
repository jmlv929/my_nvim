#批量下载Git 库
import os
import re
import git

def clone_repos(git_list):
    for _ in git_list:
        name = _.split('/',1)
        if os.path.exists(name[1]):
            print(_ + "已经存在！")
        else:
            new_repo = git.Repo.clone_from(url='git@github.com:'+ _ + '.git', to_path='./' + name[1])

def find_repo(f_file):
    f = open(f_file,encoding='utf-8')#打开文件
    t = f.read()  # 将文件的内容读取出来赋值给t
    f.close()  # 将文件关闭，如果不在代码中关闭，待会用记事本打开可能被警告被占用
    # 这时，t  是个字符串，可以对它做一般的字符串操作，比如print
    git_list_new = []
    pattern = re.compile("\"[\w-]+\/.+?\"")
    git_list = pattern.findall(t)
    git_list.sort()
    for _ in git_list:
        _new = eval(_)
        git_list.remove(_)
        if _new not in git_list_new:
            git_list_new.append(_new)
            #print("添加的库为:" + _new)
        else:
            pass
    print("添加的总数为:"+ str(len(git_list_new)))
    return git_list_new

if __name__ == '__main__':
    f_file = 'plugins.lua'
    git_list = find_repo(f_file)
    git_list = ["nshen/learn-neovim-lua"]
    clone_repos(git_list)