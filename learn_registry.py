#========================#

from winreg import OpenKey,QueryValueEx,HKEY_CURRENT_USER,CreateKeyEx

def checkCreateKeys():
    CreateKeyEx(HKEY_CURRENT_USER,"OSMANI")
    Key = OpenKey(HKEY_CURRENT_USER,"OSMANI")
    try:
        QueryValueEx(Key, "timerInterval")
    except:
        from subprocess import call
        call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                """
                New-ItemProperty  -Path  HKCU:\OSMANI\ -Name "timerInterval" -PropertyType "String" -Value '18000'
                """])
    try:
        QueryValueEx(Key, "path")
    except:
        from subprocess import call
        call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                """
                New-ItemProperty  -Path  HKCU:\OSMANI\ -Name "path" -PropertyType "String" -Value 'C:\'
                """])
    try:
        QueryValueEx(Key, "LAN_DB_SERVER ")
    except:
        from subprocess import call
        call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                """
                New-ItemProperty  -Path  HKCU:\OSMANI\ -Name "LAN_DB_SERVER" -PropertyType "String" -Value 'http://172.16.0.7:8080/0033-OCL-2020-WS/linker.php?'
                """])

    try:
        QueryValueEx(Key, "INTERNET_DB_SERVER ")
    except:
        from subprocess import call
        call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
                """
                New-ItemProperty  -Path  HKCU:\OSMANI\ -Name "INTERNET_DB_SERVER " -PropertyType "String" -Value 'http://portal.osmani.com:8049/0033-OCL-2020-WS/linker.php?'
                """])









# from winreg import OpenKey,QueryValueEx,HKEY_CURRENT_USER,SetValueEx,KEY_SET_VALUE,REG_SZ
#
#
# hKey = OpenKey(HKEY_CURRENT_USER,"OSMANI")
# result = QueryValueEx(hKey, "timerInterval")
# timer  = int(result[0])
# print(timer)
# print(type(timer))
# wKey = OpenKey(HKEY_CURRENT_USER,"OSMANI",0,KEY_SET_VALUE)
# SetValueEx(wKey, "timerInterval", 0, REG_SZ, "123")
#
#


#=================================Code from the Web=====================================#
#
# def set_run_key(key, value):
#     """
#     Set/Remove Run Key in windows registry.
#
#     :param key: Run Key Name
#     :param value: Program to Run
#     :return: None
#     """
#     # This is for the system run variable
#     reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
#
#     with reg_key:
#         if value is None:
#             winreg.DeleteValue(reg_key, key)
#         else:
#             if '%' in value:
#                 var_type = winreg.REG_EXPAND_SZ
#             else:
#                 var_type = winreg.REG_SZ
#             winreg.SetValueEx(reg_key, key, 0, var_type, value)
#
# set_run_key('NameOfNewValue', '%windir%\system32\calc.exe')
