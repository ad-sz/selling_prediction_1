# import subprocess
# from global_variables import *


# def run_powershell_data_to_sql_table(POWERSHELL_FILEPATH):
#     # command to run the script PowerShell
#     cmd = ['powershell.exe', '-ExecutionPolicy', 'Unrestricted', POWERSHELL_FILEPATH]

#     # run the script PowerShell
#     process = subprocess.run(cmd, capture_output=True, text=True)

#     # printing the results of script execution
#     print(process.stdout)

#     # if error print them
#     if process.stderr:
#         print("Errors:")
#         print(process.stderr)