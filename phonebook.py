def work_with_phonebook():

    choice=show_menu()

    phone_book=read_txt("phon.txt")
    
    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==4:
            add_user(phone_book)
            write_txt('phon.txt',phone_book)
        elif choice==5:
            last_name=input('lastname ')
            new_number=input('new  number ')
            change_number(phone_book,last_name,new_number)
            write_txt('phon.txt',phone_book)
            
   
        elif choice==6:
            last_name=input('lastname ')
            delete_by_lastname(phone_book,last_name)
            print(phone_book)
            write_txt('phon.txt',phone_book)
            phone_book=read_txt("phon.txt")


        

        choice=show_menu()
    
    print('Всего доброго!!!')

def show_menu():
    


    
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер абонента в справочнике\n"
          "6. Удалить запись\n"
          "7. Закончить работу")
    choice = int(input())
    return choice




def read_txt(filename):

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
           if line=='\n' or line=="'Фамилия': '\n'" :
                continue
           else: 
               record = dict(zip(fields, line.split(',')))
               phone_book.append(record)

    return phone_book

def find_by_lastname(phone_book,last_name):
    for line in phone_book:
        if line .get('Фамилия')== last_name:
            return (line .get('Имя'))

def find_by_number(phone_book,number):
    for line in phone_book:
        if line .get('Телефон')== number:
            return (line .get('Имя')+" " + line .get('Фамилия'))    

def add_user(phone_book):
    user_data=''
    last_name=input('введите фамилию,: ')
    user_data=user_data + last_name +','
    
    last_name=input('введите имя: ')
    user_data=user_data + last_name +','
    last_name=input('введите номер телефона: ')
    user_data=user_data + last_name +','
    last_name=input('введите описание абонента: ')
    user_data=user_data + last_name

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    print('Zapisano')
    return phone_book




def change_number(phone_book,last_name,new_number):
    for line in phone_book:
        if line .get('Фамилия')== last_name:
            print("nomer zapisan")
            line ['Телефон']=new_number
            print("nomer zapisan")
        
    
    return phone_book




def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            d='\n'
            
            for v in phone_book[i].values():
                if v!=d:
                    s = s + v + ','

            phout.write(f'{s[:-1]}\n')

    print('perepisano')


def delete_by_lastname(phone_book,last_name):
    for line in phone_book:
        if line .get('Фамилия')== last_name:
            del line['Фамилия']
            del line['Имя']
            del line['Телефон']
            del line['Описание']
            print('deleted')
    phone_book=[d for d in phone_book if d]
    return phone_book


def print_result(myList):
    for item in myList:
        
        print(item)

work_with_phonebook()


