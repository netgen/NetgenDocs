# Netgen Docs

This repository contains source code for [Netgen Docs page](https://docs.netgen.io).

## Building the docs

If any of the following steps fail, rerun the commands with `sudo`.

* Install `pip`, Python Package Manager

    On Ubuntu, you can install it with:
    
    ```
    $ apt-get install python-pip
    ```

    Otherwise, check out [official install docs](https://pip.pypa.io/en/stable/installing/).

* Install the documentation dependencies: 

    ```
    $ pip install -r requirements.txt
    ```

* In the root directory of the repo, run the following to build the docs:

    ```
    $ make html
    ```

This will build the documentation and place the generated HTML files in `_build/html` directory.
