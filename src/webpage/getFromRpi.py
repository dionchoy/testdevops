import requests
import readWriteBooks

BASE_URL = 'http://192.168.50.170:5001'

def getReserve():
    try:
        url = f'{BASE_URL}'
        response = requests.get(url)
        bookList = response.json()

        if len(bookList[list(bookList.keys())[0]][0]) == 2:
            print('test')
            readWriteBooks.changeToReserve(bookList)
            print('test2')
        elif len(bookList) == 1:
            for info in bookList:
                for book in bookList[info]:
                    readWriteBooks.removeBook(info, book[0])

    except:
        return [{}, {}]
    
    return bookList

def main():
    print(getReserve())

if __name__ == '__main__':
    main()