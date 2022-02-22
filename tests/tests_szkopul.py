from szkopulrequester import SkClient

def main():
    a = SkClient(login="login", password="password",url="https://szkopul.edu.pl/c/cslom/p/")
    a.Login()
    print(a.GetTasks(only_not_completed=True)) #pokaz zadania do zrobienia
    print(a.SendFile("link do submita mozna zdobyc z GetTasks","trz.cpp",'C++')) wyslij plik o nazwie trz.cpp
    print(a.CheckLatest(all=False))
    print(a.Ranking())#pokaz rankind
    print(a.CheckErrors("jakis link do szczegolow"))#link do tego mozna zdobyc z check latest






if __name__ == '__main__':
    main()