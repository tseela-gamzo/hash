# Hash Project

## Overview
We strive to deliver exemplary club services to both users and clothing stores. Our aim is to ensure **user privacy** while maintaining the convenience for stores. To achieve this balance, we have devised a system comprising three distinct services:

1. **club**: This service operates as the backbone of our club, responsibly managing the database with utmost reliability, security, and safety.

2. **user**: This software, embedded within the consumer's device, facilitates the transmission of club membership proof to the stores within the mall. It operates on the computational chip embedded within the club card provided to the consumer.

3. **store**: This service functions as a part of the server of the store, capable of verifying the proof sent by a club member.

Furthermore, certain information is publicly accessible, including our hash functions and the merkle root of our tree. This information can be found within the public folder.



## Installation

You can install the requirements using pip:

```bash
pip install Flask
pip install requests
```

You might also wanna install numpy:
```bash
pip install numpy
```



## Running The Code

Each `app.py` file is an executable file. For each service, there is an `app.py` file. In the case of Moadon Tov, it serves as a server. For the user service, it's a "regular" program. As for the store service, it acts as a server. However, it's important to note that this is only a component of the actual store server.

To run each file, execute the following commands in your terminal:

```bash
python club/app.py
python store/app.py
python user/app.py
```

Keep in mind that the `app.py` file for the user service **must be executed last**. This is because it communicates with both the store and Moadon Tov.
