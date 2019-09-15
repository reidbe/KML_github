from github import Github
g = Github("rei.berge@gmail.com", "snObbA2019")
org = g.get_organization('RB-KML-database')
repo = org.get_repo("test_filer")


#Lagrer ny fil til github
def save_file(filename, forklaring, filename_git = 0 ):
  if  filename_git == 0: filename_git = filename
  with open(filename, 'r') as myfile:
    tekst_fil = myfile.read()
  repo.create_file(filename_git, forklaring, tekst_fil)

#Lagrer streng som fil til github
def save_string_file(tekst_fil, forklaring, filename_git):
  repo.create_file(filename_git + '.txt', forklaring, tekst_fil)

#oppdaterer fil som finnes på github
def update_file(filename, forklaring, filename_git = 0 ):
  if  filename_git == 0: filename_git = filename
  contents = repo.get_contents(filename_git)
  with open(filename, 'r') as myfile:
    tekst_fil = myfile.read()
  repo.update_file(contents.path, forklaring, tekst_fil, contents.sha)


#save_file('a.txt', 'aaaAaaa')
#update_file('b.txt','er','a.txt')


#oppdatere en fil
#print(repo)
#contents = repo.get_contents("westcampus.kml")
#print(contents)


#https://pygithub.readthedocs.io/en/latest/examples/Repository.html#update-a-file-in-the-repository