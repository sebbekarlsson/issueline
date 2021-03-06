# issueline
> Command line issue tracker / reporter with no dependencies on Github  
> works where ever you may host your project, or just locally if one prefers that.  
> __You dont even need git.__


## Usage
> Here are some simple usage examples.  
> NOTE: _execute `issueline` from the root of your project._

### Reporting an issue
> To report an issue:

    $ issueline report --kind "bug" --title "Text changes color when clicked" --description "It probably has something to do with the javascript"

    > Your issue was created with the ID: YnVnVGV4dCBjaGFuZ2VzIGNvbG9yIHdoZW4gY2xpY2tlZEl0IHByb2JhYmx5IGhhcyBzb21ldGhpbmcgdG8gZG8gd2l0aCB0aGUgamF2YXNjcmlwdHNlYmFzdGlhbmthcmxzc29u

### Finding an issue by ID

    $ issueline query --id "YnVnVGV4dCBjaGFuZ2VzIGNvbG9yIHdoZW4gY2xpY2tlZEl0IHByb2JhYmx5IGhhcyBzb21ldGhpbmcgdG8gZG8gd2l0aCB0aGUgamF2YXNjcmlwdHNlYmFzdGlhbmthcmxzc29u"


### Listing all issues in current project

    $ issueline all

    > kind=error
    > title=Something wrong
    > description=so this happened
    > author=sebastiankarlsson
    > id=ZXJyb3JTb21ldGhpbmcgd3JvbmdzbyB0aGlzIGhhcHBlbmVkc2ViYXN0aWFua2FybHNzb24=
    > date=2018-06-27 15:24:39.404800
    > status=0

    > kind=bug
    > title=Text changes color when clicked
    > description=It probably has something to do with the javascript
    > author=sebastiankarlsson
    > id=YnVnVGV4dCBjaGFuZ2VzIGNvbG9yIHdoZW4gY2xpY2tlZEl0IHByb2JhYmx5IGhhcyBzb21ldGhpbmcgdG8gZG8gd2l0aCB0aGUgamF2YXNjcmlwdHNlYmFzdGlhbmthcmxzc29u
    > date=2018-06-27 15:29:10.015203
    > status=0

    ...

### Closing an issue
> To close an issue:

    $ issueline close --id <id>

> The `status` on the issue will now be `1`

### Open an issue
> To open an issue:

    $ issueline open --id <id>

> The `status` on the issue will now be `0`

## Where are they stored?
> By default they will be stored in a directory where executed, this directory
> is called `.issueline/` and will be created when `issueline` was executed
> for the first time.

> It is recommended __not__ to gitignore the `.issueline` directory, it is very
> neat to keep track on it using git.

## Installing
> To install `issueline`, clone down the repository and run:

    $ python setup.py install

> On some operating systems / platforms, you might have to use `sudo`.  
> You can also install it using pip:

    $ pip install issueline
