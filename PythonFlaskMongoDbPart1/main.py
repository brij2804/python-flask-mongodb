from com.brijesh.mongodb.mongodb_setup import MongoSetup


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mongosetup= MongoSetup()
    dbnames= mongosetup.show_databases()
    print_hi('PyCharm')
    print(dbnames)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
