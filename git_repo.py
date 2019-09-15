import sys
sys.path.append('/usr')

from github import Github
g = Github("rei.berge@gmail.com", "snObbA2019")
org = g.get_organization('RB-KML-database')
repo = org.get_repo("test_filer")
def save_file(filename, forklaring, filename_git = 0 ): 
  if  filename_git == 0: filename_git = filename
  with open(filename, 'r') as myfile:
    tekst_fil = myfile.read()
  repo.create_file(filename_git, forklaring, tekst_fil)


def save_string_file(tekst_fil, forklaring, filename_git):  
  repo.create_file(filename_git + '.txt', forklaring, tekst_fil)


def update_file(filename, forklaring, filename_git = 0 ):
  if  filename_git == 0: filename_git = filename
  contents = repo.get_contents(filename_git)
  with open(filename, 'r') as myfile:
    tekst_fil = myfile.read()
  repo.update_file(contents.path, forklaring, tekst_fil, contents.sha)
