from models.Items  import Item
from models.Pos import POS
import  csv


def main():
    a =  csv.DictReader(open('data.csv'))

    for row in a:
        print('i need to learn linear algebra')

   


if __name__ == "__main__":
    main()
