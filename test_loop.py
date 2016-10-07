for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if (root==os.getcwd()):
            if (str(file)[-4:]=='.png'):
                print file