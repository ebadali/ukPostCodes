# Project Title

This is a python application for validation and formating the Uk [Post codes](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

```
1. python 2.7+/3.6+
2. Make: https://www.gnu.org/software/make/
```

### Installing


```
1. git clone https://github.com/ebadali/ukPostCodes.git 
2. cd ukPostCodes
3. make init
```

### Usage

Import the library
```
from postcodes import validatePostCode,formatPostCode
```

Calling the functions
```
# validating a postcode
validatePostCode(postcode)

# Formating a postcode
formatPostCode(postcode)
```

Example
```
from postcodes import validatePostCode,formatPostCode

print(validatePostCode('AA9A 9AA'))

print(formatPostCode('AA9A9AA'))

```


## Running the tests

```
make test
```

## Built With

* [python2.7](https://www.python.org/download/releases/2.7/) - The Language used
* [nosetest](http://nose.readthedocs.io/en/latest/) - Testing framework

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Ebad Ali** - *Initial work* - [Profile](http://ebadali.com/EbadAliSoftwareEngineer.html)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

