# Introduction 
This project aims at creating a wrapper for code/libraries used by the camera system which are written in C and need to be launched using ROS. By wrapping the code in python, the camera's code will be better integrated and the use/the launch of the camera system will be simpler and more intuitive.

In the begining, the goal is to test how different wrapping methodes (manual=by hand, SWIG, cython) work using simple examples and conclude on which one is the most adapted for Lifeline Robotic's case.

Conclusion on the methodes used :
- manual wrapping is pointless for large code structures since it takes a lot of time resources and there are simply better ways to do it
- cython is a tool adapted for making the python code run faster thanks to C's fast comilation proprietes. It is mostly used to convert python code into C.
- SWIG lets the user convert c/cpp code into different programming languages. Using SWIG requires creating a .i (interface) file to specify the code the user would like to wrapp. There is also more resources available online. Personally, I recommend watching this video to get aqueinted with the concept of c/cpp - python integration and the use of SWIG : https://www.youtube.com/watch?v=J-iVTLp6M9I

I belive SWIG to be the best tool for Lifeline Robotic's case of wrapping camera's c/cpp libraries into python.

# Getting Started
1.	Installation process
Install SWIG
2.	Software dependencies
None, just different ways of installing SWIG.
3.	Latest releases
4.	API references

# Build and Test
Build : 
make sure to put the c/cpp code in a src folder and to create a .i (interface) file.

Test : 
Go to swig_c_test or swig_cpp_test and comiple the X.i file using the command line : 
swig -python -Isrc X.i

# Contribute
TODO: Tests are done, it's time to wrap camera's libraries in python. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)
