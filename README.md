# Multi-Party Computation Cryptography - Final Project

![Project Logo](logo_link)

- [Multi-Party Computation Cryptography - Final Project](#multi-party-computation-cryptography---final-project)
  * [About](#about)
  * [What is Multi-Party Computation (MPC)?](#what-is-multi-party-computation--mpc--)
  * [Authors](#authors)
  * [Project Overview](#project-overview)
  * [Project Goal](#project-goal)
  * [Introduction](#introduction)
  * [Methods & Algorithms](#methods---algorithms)
    + [Design Considerations](#design-considerations)
    + [Selected approach](#selected-approach)
  * [Pseudo Code Bit OR](#pseudo-code-bit-or)
    + [Procedure PrivacyPreservingBitOr:](#procedure-privacypreservingbitor-)
    + [Infrastracture](#infrastracture)
    + [User Interface](#user-interface)
  * [Development proccess](#development-proccess)
  * [API Reference](#api-reference)
      - [Get item](#get-item)
      - [add(num1, num2)](#add-num1--num2-)
  * [Appendix](#appendix)
  * [License](#license)
  * [Tech Stack](#tech-stack)
  * [Usage/Examples](#usage-examples)
  * [Demo](#demo)
  * [Deployment](#deployment)
  * [Environment Variables](#environment-variables)
  * [Run Locally](#run-locally)
- [Files & Project structure](#files---project-structure)
- [Synchronization](#synchronization)
  * [Manage file synchronization](#manage-file-synchronization)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>




## About

This project is an implementation of a secure multi-party protocol for the secure set-union problem and the secure all-pairs shortest path problem. The protocol is devised from existing literature and is tailored for enhanced efficiency in a semi-honest setting with a dishonest majority.

## What is Multi-Party Computation (MPC)?

Multi-Party Computation (MPC) is a subfield of cryptography that enables multiple entities to jointly compute a function over their inputs while keeping those inputs private. In the context of this project, we focus on a 2-party computation, where both entities share inputs and follow the MPC protocol, ensuring the privacy of their inputs.


## Authors
- [@Dolev Dublon](https://www.github.com/dolev146)
- [@Yakov Khodorkovski](https://github.com/yakov103)


## Project Overview

## Project Goal

The primary objective of this project is to implement a secure multi-party protocol that is specifically designed for the secure set-union problem and the secure all-pairs shortest path problem. Our protocol aims to achieve greater efficiency than generic MPC protocols, especially in semi-honest settings with a dishonest majority. We base our approach on existing research by Justin Brickell and Vitaly Shmatikov, which you can access [here](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/blob/main/shmat_asiacrypt05.pdf).


## Introduction

Our protocol deals with two semi-honest groups. Since the late 1980s, general protocols have theoretically allowed secure computation in polynomial time and with a security parameter, enabling both players to compute safely under computational complexity assumptions. While these general protocols are theoretically efficient, they are not always practically efficient. Therefore, people have been trying to create specific security protocols for specific functions that are more efficient than the general protocols.​

The use of various generic libraries, such as YAO, and GMW, has proven to be less efficient, prompting efforts to develop more efficient approaches. We will implement the All-Pairs Shortest Path functionality to contribute to the ecosystem of implementations, aiming to create more efficient implementations in this domain.

## Methods & Algorithms

### Design Considerations
***There were two algorithms for the set union to implement in our protocol:***
1. A provided pseudocode that utilized YAO and GMW for the calculation of the minimum using a generic library. However, this did not fit with our chosen programming language.​
2. A tree pruning method that utilized ElGamal and BitOr to reveal information securely.

### Selected approach
**We have decided to implement the BitOr operation to achieve a union without relying on a generic library. **
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
The users for the library that we developed are Software developers
Our goal wasn't to build an application for everybody's use, but we decided to also provide a visual representation and an infrastructure to help future developers understand how to implement the use of our work inside their software. and also to provide an overview for people outside the Multi-party computation as a way to see our work runs in actions
Our simple, user-friendly interface provides transparency into the protocol's progress and status, and execution providing a log output to see the full process.

Insert screens here

[ QR code for GitHub repo on bottom-right ]


## Development proccess


  

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

  

Insert gif or link to demo


  

## Deployment

  

To deploy this project run

  

```bash

npm run deploy

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

npm install

```

  

Start the server

  

```bash

npm run start

```


# Files & Project structure



# Synchronization

Synchronization was one of our biggest obstacle

## Manage file synchronization

To manage it we used Kanban board





notes https://docs.google.com/document/d/1d35ExjbP7p1KzuKcKIswkkOI2wedrJmxIr1OTyWHQyg/edit# 

