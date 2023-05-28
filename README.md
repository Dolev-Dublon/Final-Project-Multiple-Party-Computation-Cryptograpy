# Multi-Party Computation Cryptography - Final Project

* finish writing the development process api and demo and screenshots adding tests
* fix the SSD document https://docs.google.com/document/d/1oWhDiyfaaCHef23QWVzcB4Yah-8EvjGF3wODgSoSex4/edit#

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

<img src="https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/0e4c30fe-6703-43d7-b91f-f775ecc49dd2" width=400px  />

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

## Vision Statement - MPC protocol implementation

[Vision Statement](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/blob/main/Vision%20Statement.pdf)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/3e22173b-be80-4746-b7b7-4db4799b849f)

## SRD Document

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/09dcdd56-e8ba-45f1-ba25-8544524c27b4)
![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/ef478b28-d05c-4edd-b201-ab6fc9e814ee)
![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/9f4f8271-74f1-41b4-a672-8fdd11575010)
![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/70a49f9d-c8ce-4830-b104-e681c543bde3)



## Privacy-Preserving Graph Algorithms in the Semi-honest Model 
by Justin Brickell and Bitaly Shmatikov
The University of Texas at Austin, Austin TX 78712, USA

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/2654a3ec-b54b-453b-b145-715c0d433361)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/2b57663d-4d07-4970-b9a8-461075e4aef6)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/a8e72665-b145-4e67-bcec-b88d4981f38f)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/0116c98b-50b0-46af-be92-e9f66279912b)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/dcbdc241-2316-4271-9546-da2dad9aba5d)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/335b4709-193f-4864-9ba1-81212f662828)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/af600236-eb82-45d4-8e11-603cb28979c1)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/552b3d33-a234-4f97-8ab8-3418add22251)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/20ca3c72-9c7e-47a5-b7e6-e7b288867e3f)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/91939058-7fda-48c8-be64-9b29695398c9)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/97d7ebbb-c5e0-40f6-80e7-4fbd70c6f7e7)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/0dffe14f-ba64-488f-a231-d85d394dbf5a)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/e4cf9373-1415-4eb5-9ca0-da23227695a3)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/f91500cd-673f-4039-a87e-f89c6666201d)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/c266f0f4-2981-44ea-81e8-1dd979774881)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/9dc89741-eb14-45b0-a60a-0177618f470e)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/4a9c9bec-558b-4dad-addb-df39eead53ff)

## A Proof of Security of Yao’s Protocol for Two-Party Computation
by Yehuda Lindell∗ Benny Pinkas June 26, 2006

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/0e7a292c-7a5b-480e-ab81-da043b70b404)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/780f2e66-5728-4b98-a4ad-75f50cee0654)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/dc2ab284-266c-4b89-804f-4e2362f924b3)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/e3bbfad1-1b5e-46ff-95e8-5b7df34b7aeb)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/7b758edc-d86e-41d3-afb8-86908928d64d)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/ca574f7f-6c70-4cd7-b655-b489942574dd)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/5780f0db-ff62-4681-a53d-453bda441eb5)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/3f1cc5fe-3687-4d50-8903-90cd480a1652)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/cbe47ad0-de81-4abf-a871-36397b17512a)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/1eb3e8da-3483-4a4b-a0a7-c65aba6e6adc)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/0218a6d6-353e-4928-8063-dd6475962420)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/a15dbe0e-1ed8-450a-b4a6-ab16ea817569)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/0358a39f-3c52-4840-b33f-edc8f904479d)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/686aaadf-de8f-4e42-a833-c685f7ae84ab)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/b7416f62-096f-4cea-9961-d3455a0b7b90)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/1e03d6b8-4425-411b-82b5-3b4c908ff0f6)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/af317636-cb29-4f17-9cbf-13b9b468ff37)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/f0fb1300-5982-4626-8128-61cf5a958fac)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/2ca61858-3b15-4835-9ddb-7168f1301c5b)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/b99430ae-bce6-41fb-990f-04ca7bccc52e)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/9aecc0d6-0213-4869-bbdc-98a2a30f6f13)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/dab391c2-608f-46d7-851f-0107bb8696d2)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/ec44d686-e41b-4ad6-9051-7905bedd3c59)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/585ba500-db60-4887-8963-d60172741707)

![image](https://github.com/Dolev-Dublon/Final-Project-Multiple-Party-Computation-Cryptograpy/assets/62290677/2936c444-bf5a-4671-b66f-7207a3fd7645)












##### notes
- notes for final project https://docs.google.com/document/d/1d35ExjbP7p1KzuKcKIswkkOI2wedrJmxIr1OTyWHQyg/edit# 
- vistion statements notes https://docs.google.com/document/d/1xL3wtaWKGzi0FGTweE9COot-9TdP_mHv4BdzA2mkEAg/edit?usp=sharing 
- SSD https://docs.google.com/document/d/1oWhDiyfaaCHef23QWVzcB4Yah-8EvjGF3wODgSoSex4/edit?usp=sharing 
- SRD https://docs.google.com/document/d/1w5ZWddqB6iOTN4Ku2wOdZLmmxYpQKhgURkkDfFiViZY/edit?usp=sharing


