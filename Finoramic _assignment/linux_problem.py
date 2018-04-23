import pip, json

def install_package(package):
    return pip.main(['install', package])
with open('/home/ramesh/PycharmProjects/python_learning/Finoramic assignment/project dependencies.json') as fn:
    data = json.load(fn)
    dependencies =  data['Dependencies']
    failed_packages=[]
    successfull_packages=[]

    for package in dependencies:
        status = install_package(package)
        if status == 1:
            failed_packages.append(package)
        else:
            print("Successfully installed Package: ",package)
    print("Failed packages:",failed_packages)