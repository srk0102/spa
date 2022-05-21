def find(path, fileName):
  recursivePath = path.strip("/").split("/")
  if(recursivePath[0] != fileName and len(recursivePath)>1):
    print(recursivePath[0])
    recursivePath.pop(0)
    return find("/".join(recursivePath) , fileName)
  else:
    print(fileName)

path = input()
fileName = input()
find(path, fileName)
input()