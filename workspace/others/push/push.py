import os
from modules.MyGit import MyGit
from modules.MyFormat import MyFormat
from modules.MyView import MyView

message = "VuVanNghia20206205"

git =  os.path.join(os.getcwd(), '../../../')
contents =  os.path.join(os.getcwd(), '../../../baocao/contents')
main =  os.path.join(os.getcwd(), '../../../baocao/contents/main')
# init_path =  os.path.join(os.getcwd(), '../../../baocao/contents/start/init.sty')
# workspace_path = os.path.join(os.getcwd(), '../../report.code-workspace')
# gitignore_path = os.path.join(git_path, ".gitignore") 

MyGit.chdir(git)
MyGit.add()
MyGit.commit(message)

MyFormat.latex(contents)
MyFormat.latex(main)
# MyFormat.markdown(git_path)
# MyFormat.basic(gitignore_path)
# MyFormat.basic(init_path)
# MyFormat.workspace(workspace_path)

MyView.CloseTab()
MyView.Target(2)
MyView.CloseTerminal()
MyView.CloseScrollBar()
# MyView.CollapseFolders()
# MyView.OpenGit()
MyView.OpenLatex()
