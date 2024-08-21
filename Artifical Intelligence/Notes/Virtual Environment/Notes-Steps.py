"""
To create a virtual environment you first need to create a directory to put it in. (I'm using this for usbs')
then you will need to use this code 
    python -m venv NameOfEnvironment-env
    
        To activate the environment 
            * On windows
                py -m venv dir
                NameOfEnvironment-env\Scripts\activate.bat 

                virtualenv dir 
                dir\Scripts\activate

                    or
                
                dir\Scripts\activate 


            * On Unix or MacOS, run: 
                source NameOfEnvironment-env/bin/activate 

                - the script is written for bash, shell. If you use the csh or fish shells, there are alternate activate.csh and activate.tish scripts you should use instead.)
        
        python -m pip show
            will display information about a particular package 
        
        python -m pip list 
            will display all of the packages installed in the virtual environment 

        python -m pip freeze will produce a similar list of the installed packages, but the output uses the format that python -m pip install expects. A common convention is to put this list ina requirements.txt file: 

        requirements.txt can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r. 

        To deactivate a virtual envirionment type 
            deactivate 
                into the terminal 
        
        python -m pip install NameOfPackage 
            will install the latest version of a module and its dependecies from the Pytyon Package Index: 

        python -m pip install --upgrade NameOfPackage 

    Remember - Creation of virtual environments is done through the venv module. Installing packages into an active virtual environment uses the commands shown above. 
    
    Passing the --user option to python -m pip install will install a package just for the current user, rather than for all users of the system. 

    if pip is not installed by default try this 
        python -m ensurepip --default-pip 

    Installing from a local src tree 
        py -m pip install -e <path>

    You can also install normally form src 
        py -m pip install <path> 

    Installing from other sources 
        ./s3helper --port=7777 
        python -m pip install --extra-index-url http://localhost:7777 SomeProject 

    Installing from local archives 
        py -m pip install ./downloads/SomeProject-1.0.4.tar.gz 

    Installing from other Indexes 
        
        py -m pip install --index-url http://my.package.repo/simple/ SomeProject 
        
    
    """