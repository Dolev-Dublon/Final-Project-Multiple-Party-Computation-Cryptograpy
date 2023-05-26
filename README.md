# Multi-Party Computation Cryptography - Final Project


<img src="https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/d7f77a75-62cb-42c5-a6e1-dce23579a213" width=150px />

|<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" /> |<img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" /> |<img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white" />  |
|-|-|-|
|<img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white" /> | <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> | <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> |
|<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" /> | <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" /> | <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /> |


![tenor](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/b900f69f-0f6e-4a04-a579-478dfcbc34ba)
- [Multi-Party Computation Cryptography - Final Project](#multi-party-computation-cryptography---final-project)
  * [About](#about)
  * [What is Multi-Party Computation (MPC)?](#what-is-multi-party-computation-mpc)
  * [Authors](#authors)
  * [Project Overview](#project-overview)
  	* [Project Goal](#project-goal)
  	* [Introduction](#introduction)
  	* [Methods & Algorithms](#methods--algorithms)
  		* [Design Considerations](#design-considerations)
  		* [Selected approach](#selected-approach)
  	* [Pseudo Code Bit OR](#pseudo-code-bit-or)
  		* [Procedure PrivacyPreservingBitOr:](#procedure-privacypreservingbitor)
  		* [Infrastracture](#infrastracture)
    		* [User Interface](#user-interface)
  * [Development proccess](#development-proccess)
  * [API Reference](#api-reference)
  	* [Get item](#get-item)
  	* [add(num1, num2)](#add-num1--num2-)
  * [Appendix](#appendix)
  * [License](#license)
  * [Tech Stack](#tech-stack)
  * [Usage/Examples](#usageexamples)
  * [Demo](#demo)
  * [Environment Variables](#environment-variables)
  * [Run Locally](#run-locally)
- [Files & Project structure](#files--project-structure)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>




## About

This project is an implementation of a secure multi-party protocol for the secure set-union problem and the secure all-pairs shortest path problem. The protocol is devised from existing literature and is tailored for enhanced efficiency in a semi-honest setting with a dishonest majority.

## What is Multi-Party Computation (MPC)?

[Multi-Party Computation (MPC)](https://en.wikipedia.org/wiki/Secure_multi-party_computation) is a subfield of cryptography that enables multiple entities to jointly compute a function over their inputs while keeping those inputs private. In the context of this project, we focus on a 2-party computation, where both entities share inputs and follow the MPC protocol, ensuring the privacy of their inputs.
***Without the intervention of a server (Third party) in the proccess.***
<img src="https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/c410f5db-4c8a-449f-9cb7-777628cf9003" width=400px style="width: 150px; height: 150px; object-fit: cover; object-position: 25% 25%; " />


## Authors
- [@Dolev Dublon](https://www.github.com/dolev146)
- [@Yakov Khodorkovski](https://github.com/yakov103)
- [@Daniel Zaken](https://github.com/aaaa)
- [@Aviad Gilboa](https://github.com/aaaa)


## Project Overview

## Project Goal

The primary objective of this project is to implement a secure multi-party protocol that is specifically designed for the secure set-union problem and the secure all-pairs shortest path problem. Our protocol aims to achieve greater efficiency than generic MPC protocols, especially in semi-honest settings with a dishonest majority. We base our approach on existing research by Justin Brickell and Vitaly Shmatikov, which you can access [here](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/blob/main/shmat_asiacrypt05.pdf).


## Introduction

Our protocol deals with two semi-honest groups. Since the late 1980s, general protocols have theoretically allowed secure computation in polynomial time and with a security parameter, enabling both players to compute safely under computational complexity assumptions. While these general protocols are theoretically efficient, they are not always practically efficient. Therefore, people have been trying to create specific security protocols for specific functions that are more efficient than the general protocols.

The use of various generic libraries, such as YAO, and GMW, has proven to be less efficient, prompting efforts to develop more efficient approaches. We will implement the All-Pairs Shortest Path functionality to contribute to the ecosystem of implementations, aiming to create more efficient implementations in this domain.

## Methods & Algorithms

### Design Considerations
***There were two algorithms for the set union to implement in our protocol:***
1. A provided pseudocode that utilized YAO and GMW for the calculation of the minimum using a generic library. However, this did not fit with our chosen programming language.
2. A tree pruning method that utilized ElGamal and BitOr to reveal information securely.

### Selected approach
**We have decided to implement the BitOr operation to achieve a union without relying on a generic library.**

| Image | Cryptographer | Link |
|:-----:|:-------------:|:----:|
| <img src="https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/d45f6e6d-8011-4830-bebd-650de1939874" width=100px /> | Elgamal | [Wikipedia](https://en.wikipedia.org/wiki/Taher_Elgamal) |
| <img src="https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/e060f372-03ca-4be6-bec9-08e05008602d" width=100px /> | Yao | [Wikipedia](https://en.wikipedia.org/wiki/Andrew_Yao) |




because the iterative method required using a generic library to calculate the minimum in a secure way.

## Pseudo Code Bit OR

### Procedure PrivacyPreservingBitOr:
1. Alice initializes:
	- Selects cyclic group $G$ of prime order $q$
	- Chooses $g$ (quadratic residue) and large prime p $(p=2q+1)$
	- Chooses private key $k ∈ \{0, ..., q-1\}$
	- Picks random $r ∈ \{2, ..., q-1\}$
	- If Alice's bit is $0$, calculates $C_a = (g^r, g^{(kr)})$
	- If Alice's bit is $1$, calculates $C_a = (g^r, g\cdot g^{(kr)})$
2. Alice sends $(C_a, q, g, g^k)$ to Bob, keeping k private
3. Bob receives $(C_a, q, g, g^k)$ and unpacks $C_a$ into $(α, β)$
	- Picks random $r' ∈ \{2, ..., q-1\}$
	- If Bob's bit is $0$, calculate C_b = (α^r', β^r')
	- If Bob's bit is $1$, calculate C_b = (α^r', g^r'*β^r')
4. Bob sends $C_b$ back to Alice
5. Alice receives $C_b$, unpacks it into $(γ, δ)$
	- Calculates $b = \frac{δ}{γ^k}$
		- If $b = 1$, returns $0$
		- If $b ≠ 1$, returns $1$
insert diagram here

### Infrastracture
**Using Flask and Gunicorn servers on cloud platforms of Microsoft Azure. we represent parties involved in the secure computation.**

### User Interface 
We built a library mainly for software developers, but included visual aids and infrastructure for easier understanding. It's designed to show anyone how our system works, especially in Multi-party computation. Our simple interface gives a clear view of the protocol's progress and even includes a log output to follow the entire process.

Insert screens here

[ QR code for GitHub repo on bottom-right ]


## Development proccess

At first the Development process was to read a lot and get deep into the article of Justin Brickell and Vitaly Shmatikov, which you can access [here](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/blob/main/shmat_asiacrypt05.pdf).
and we met every week from the begining reading it, and also reading the article [A Proof of Security of Yao’s Protocol for Two-Party Computation]() by Yehuda Lindell Benny Pinkas and we had to learn a lot about the secure computation proofs and theory [Semi-Honest Adversaries](https://www.youtube.com/watch?time_continue=2&v=z3U-5mf6hGw&feature=emb_title) and this lecture as well.
This is the first step is to get into the field so we can understand the problem more deeply.
then we wrote the 


Synchronization was one of our biggest obstacle for us as a team and for the threads in the program between the clients

  

## API Reference

```http
GET /api/datapoint

```
| Parameter | Type | Description |

| :-------- | :------- | :------------------------- |

|  `api_key`  |  `string`  |  **Required**. Your API key |

  

#### Get item

  
```http

GET /api/items/${id}

```

| Parameter | Type | Description |

| :-------- | :------- | :-------------------------------- |

|  `id`  |  `string`  |  **Required**. Id of item to fetch |

  

#### add(num1, num2)

  

Takes two numbers and returns the sum.
  

## Appendix

Any additional information goes here

  

## License

[MIT](https://choosealicense.com/licenses/mit/)

  

## Tech Stack

**Client:** HTML CSS JAVASCRIPT, Jinja engine for flask
**Server:** PYTHON FLASK

  

## Usage/Examples

  

```javascript

import  Component  from  'my-project'

  

function  App()  {

return  <Component />

}

```

  

## Demo

  
Insert gif *and* image for the video demo on youtube

  

## Deployment

1. get a user on Microsoft Azure
2. 

  

To deploy this project run

  

```bash

gunicorn 

```


## Environment Variables

  

To run this project, you will need to add the following environment variables to your .env file

  

`API_KEY`

  

`ANOTHER_API_KEY`

  

## Run Locally

  

Clone the project

  

```bash

git clone https://link-to-project

```

  

Go to the project directory

  

```bash

cd my-project

```

  

Install dependencies

  

```bash

pip install flask .....

```

  

Start the server

  

```bash

npm run start

```


# Files & Project structure



# Documents





notes https://docs.google.com/document/d/1d35ExjbP7p1KzuKcKIswkkOI2wedrJmxIr1OTyWHQyg/edit# 


