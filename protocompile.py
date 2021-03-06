import os 


class Trc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
prompt ='> '
compileCalled =False
protoFolderFound = False
protoFileFound = False
outputFolderFound = False

print(f'{Trc.HEADER}Paste Projects Complete Directory{Trc.ENDC}')
projectDir = input(prompt)

os.chdir(r"{}".format(projectDir))
while compileCalled == False:
    # Get User Input To Generating client and server code
    while protoFolderFound == False:
        print(f"{Trc.OKGREEN}In what Folder dir is the proto file located?{Trc.ENDC}")
        folderLocation = input(prompt)
        pathExists = os.path.exists(folderLocation) 
        if pathExists ==False:
            print(f"{Trc.FAIL}\n==> Folder Does Not Exist !!\n{Trc.ENDC}")
            compileCalled =False
            protoFolderFound =False
            continue
        else:
            protoFolderFound =True
    while protoFileFound == False:
        print(f"{Trc.OKGREEN}What is your Proto file name ?{Trc.ENDC}")
        fileName = input(prompt).removesuffix('.proto')
        filepath =f'./{folderLocation}/{fileName}.proto'
        fileExists = os.path.exists(filepath)
        if fileExists == False:
            print(f"{Trc.FAIL}\n==> Proto file does not exist !!\n{Trc.ENDC}")
            compileCalled =False
            protoFileFound =False
            continue
        else:
            protoFileFound =True
    while outputFolderFound == False:
        print(f"{Trc.OKGREEN}Folder name for Generating client and server code ?{Trc.ENDC}")   
        outputfolder = input(prompt)   
        outputhFolderExists = os.path.exists(outputfolder) 
        if outputhFolderExists ==False:
            print(f"{Trc.FAIL}\n==> Folder Does Not Exist and will be Created !!\n{Trc.ENDC}")
            os.system(f'mkdir {outputfolder}')
            outputhFolderExists = os.path.exists(outputfolder)
            if outputhFolderExists ==False:
                print(f"{Trc.FAIL}\n==> Folder Does Not Exist and could not be Created !!\n{Trc.ENDC}")
                compileCalled =False
                outputFolderFound = False
                continue
            else:
                compileCalled=False
                outputFolderFound=True
        else:
            compileCalled=False
            outputFolderFound=True
    try:    
        inputCommand =f"python -m grpc_tools.protoc -I ./{folderLocation} "
        pythonOutputFolder=f"--python_out=./{outputfolder}/ "
        GrpcOutputfolder=f"--grpc_python_out=./{outputfolder}/"
        ProtoFolderLocation=f" ./{folderLocation}"
        fileNameCommand =f"/{fileName}.proto"
        CompilerCommand= f'{inputCommand}{pythonOutputFolder}{GrpcOutputfolder}{ProtoFolderLocation}{fileNameCommand}'
        os.system(CompilerCommand)
        print(f"{Trc.OKGREEN }Generating client and server code Complete{Trc.ENDC}")    
        compileCalled =True 
    except Exception as e :
        print(f'{Trc.FAIL}{e}{Trc.ENDC}')


