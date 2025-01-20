from szkopulpylib.szkopul import SkClient

def main():
    a = SkClient(login="login", password="pass",url="https://szkopul.edu.pl/c/plockie-treningi-olimpijskie/p/")
    a.Login()

    print(a.Ranking()) # pokaz ranking
    print(a.GetTasks()) # pokaz zadania do zrobienia
    print(a.SendFile("link do submita danego zadania","trz.cpp",'C++')) # wyslij plik o nazwie trz.cpp
    print(a.CheckLatest(all=False))
    print(a.CheckErrors("link")) # link do tego mozna zdobyc z check latest


if __name__ == '__main__':
    main()
