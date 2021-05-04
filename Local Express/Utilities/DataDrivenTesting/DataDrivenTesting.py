from Utilities.DataDrivenTesting import XLUtils
import TestData.ENVs

def getLogInAndPasswordsFromFile() -> list:
    path = TestData.ENVs.Env.logInDataFilePath
    rows = XLUtils.getRowCount(path, "UsersList")
    logInAndPasswordsList = []
    for r in range(2, rows+1):
        username = XLUtils.readData(path, "UsersList", r, 1)
        password = XLUtils.readData(path, "UsersList", r, 2)
        result   = XLUtils.readData(path, "UsersList", r, 3)
        user = {
            "userName" : username,
            "password" : password,
            "result"   : result
        }
        logInAndPasswordsList.append(user)

    return logInAndPasswordsList
