# MMT
This repository is about making a python app to help in basic math modeling. It has as a contraint to be a completly modular application


## Table of contents
[Technologies](#Technologies)

[Content](#Content)

[Specifications](#Specifications)

[Project-Status](#Project-Status)

[Change-Log](#Change-Log)

[Sources](#Sources)


### Technologies
Language : Python

Environement : Visual Studio Code

License : MIT


### Content
For now, none


### Specifications
#### Main Objective
The program has to allow anyone with it to make basic math modeling (after stated as mm) in an easy way. It should allow the user to use it in any conditions where mm could be needed. It should not let the user have to make any of the work at its place. It should also be modular, to make it easy to add new features.

#### Math technologie to be used
- Solutions estimation
  - [ ] Newton-Raphson solution estimation
  - [ ] Secant method
- Primitive estimation
  - [ ] Midpoint method
  - [ ] Crank-Nicolson
- Derivative estimation
  - [ ] Finite difference method
  - [ ] Partial derivatives
- Polynomial interpolation
  - [ ] Lagrange basis
  - (Optional) Newton basis

#### Computer technologie to be used
The program has to be modular. The main program is the main module, and will only manage launching other module depending on their types. The types are the folowing :

##### Backend module
**characteristics**<br>
- no dependencies exept for the main module
- gives a librarie of backend functions
- main user of the math-tech

##### Graphic module
**characteristics**<br>
- Backend and main module as dependencies
- gives librarie of frontend or 'executable' functions

##### UI module
**characteristics**<br>
- Backend and Graphic dependencies
- Manage the UI with the function given by libraries

##### Architecture
###### Main module
Source<br>
├─ main.py<br>
├─ module_loaders.py<br>
├─ errors.py<br>
├─ option.dat<br>
├─ modules<br>
└─ └─ ...module_folders...<br>

###### Module folder
Module name<br>
├─ dependencies.info<br>
├─ lib.info<br>
├─ module_name.py<br>
└─ ...<br>

##### Installer
The installer should have no dependencies, and if possible should not need any internet. The user should be allowed to choose which module he want to have, the installer setting up the choosen modules and its dependencies.

##### Errors
An simple error managment should be active, using as identifier three indicators, including two id (file/module id and error id), and the weigh of the error.

##### Options
Depending on options, the app react differently. It should be managable inside the app, but also as a readible file



### Project-Status
[Version](#Change-Log) - 0.0.1

Size - 112 Kb

Current Dev - [@lLouu](https://github.com/lLouu)



### Change-Log
#### V0.0.1
 - github setup & .github folder
 - README & specifications

### Sources
EFREI Courses (I'm afraid, that's private knowledge)