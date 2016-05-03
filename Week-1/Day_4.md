# Day-3

## Day-2 Review
비선형 - 트리, 그래프
차이점
트리 - root가 있다
그래프 - root가 없다

데이터베이스 - 관계형, 키-값형, 객체형

## 네트워크 & 암호화
### 네트워크

Types of Computer Network
- LAN, MAN, WAN

Newtwork Architecture
- Client/Server, Peer to Peer

Network Topologies
- Star, Ring, Bus

LAN
- Local Area Network
- 근거리 통신망

MAN
- Metropolitan Area Network

WAN
- 광역통신망
- 주(States) 단위

인터넷
- Inter Network
- 컴퓨터로 연결하여 TCP/IP 프로토콜을 이용해 정보를 주고받는 컴퓨터 네트워크

TCP/IP
- TCP(Transmission Control Protocol)
- IP(Internet Protocol)
통신할때 쓰는 통신규약

WWW
- World Widw Web
- 문서(웹페이지)들이 있는 정보의 저장소
- 분산과 연결
- 정보의 분산과 연결

그럼 **왜 분산을 해놓았나?**
심심해서 분산시킨것도 아니고 대체 왜
- 정보가 어떤 한곳에 뭉쳐있으면 그것들을 제어/관리하기가 어렵다. 또한 그 유일의 하나가 무너지면 복구하기가 어렵다.
- 각 반마다 담임이 있고, 각 담임들은 자신의 반에 대한 정보를 가지고 있다.
 -> 담임들은 정보를 공유함으로 각 반에 대한 정보를 알 수 있다.

URL
- Uniform Resource Locator
- [Protocol]://[Host]:[Port]/[Path]

| URL | URI |
|--------|--------|
|     Uniform Resource Locator   |     Uniform Resource Identifier   |
| 파일리소스를 가리킴 | 식별자를 가리킴|
| http://test.com/sample.pdf | http://test.com/company|
| 웹사이트 상의 파일| RESTful 서비스 |

URI = URL + URN
URI > URL 포함되는 범주
모든 URL은 URI이다(True)


Protocol
- 프로토콜
- 통신규약
- 장비 사이에서 메시지를 주고 받는 양식과 규칙의 체계 즉, 통신(네트워킹)할 때 정해진 메세지 규칙
- http, https, ftp, sftp, telnet

HTTP
- Hyper Text Transfer Protocol

HTTPS
- Hypertext Transfer Protocol over Secure Socket Layer
- HTTP의 SSL이 들어간 개념

SSL(Secure Socket Layer)
- 전송계층의 암호화 방식

SSL 과정 설명
1. [웹브라우저] SSL로 암호화된 페이지를 요청하게 된다. (일반적으로 https://가 사용된다)

2. [웹서버] Public Key를 인증서와 함께 전송한다.

3. [웹브라우저] 인증서가 자신이 신용있다고 판단한 CA(일반적으로 trusted root CA라고 불림)로부터 서명된 것인지 확인한다. (역주:Internet Explorer나 Netscape와 같은 웹브라우저에는 이미 Verisign, Thawte와 같은 널리 알려진 root CA의 인증서가 설치되어 있다) 또한 날짜가 유효한지, 그리고 인증서가 접속하려는 사이트와 관련되어 있는지 확인한다.

4. [웹브라우저] Public Key를 사용해서 랜덤 대칭 암호화키(Random symmetric encryption key)를 비릇한 URL, http 데이터들을 암호화해서 전송한다.

5. [웹서버] Private Key를 이용해서 랜덤 대칭 암호화키와 URL, http 데이터를 복호화한다.

6. [웹서버] 요청받은 URL에 대한 응답을 웹브라우저로부터 받은 랜덤 대칭 암호화키를 이용하여 암호화해서 브라우저로 전송한다.

7. [웹브라우저] 대칭 키를 이용해서 http 데이터와 html문서를 복호화하고, 화면에 정보를 뿌려준다.

Hyper Text
- 링크를 통해 독자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

FTP
- File Transfer Protocol

TELNET
- TErminaL NETwork
- 원격 로그인을 위한 프로토콜
- 보안 수준 낮음

SSH
- Secure Shell
- 네트워크 상의 다른 컴퓨터에 로그인
- Telnet의 대용 목적

SMTP
- Simple Mail Transfer Protocol
- 전자메일 발송 프로토콜

Hostname
- 네트워크에 연결된 장치에 부여되는 고유한 이름
- IP주소, 도메인 주소

Port
- 가상의 논리적 통신 연결단
- 번호로 구분

Port-Fowarding
- 다른 포트(123)의 패킷들을 내가 원하는 포트(234)로

OSI 7계층
Open Systems Interconnection Reference Model

(사용자)
응용
표현
세션
전송
네트워크
데이터 링크
물리
(물리적인 것들(랜선))

아래로 갈수록 데이터에 포함되는 데이터가 많아짐

192.168.x.x <- 내부 IP

포트가 열려있는지 하나씩 다 찔러봄 - 해커

서브넷 마스크


0과1인 이유
- 간섭이 심해서


PUT - 데이터를 올려준다

## 암호화
- 대칭키 - 같은 키로 암호화/복호화
- 공개키(비대칭키)
- 암호화 해시 함수

대칭키
- 암호화에 복호화에 같은 암호키를 쓰는 알고리즘
- DES, AES, SEED

공개키(비대칭키) 암호화
- 사전에 비밀키를 나눠가지지 않은 사용자들이 안전하게 통신할 수 있도록 하는 암호화 알고리즘
- RSA등

암호화 해시 함수
- 임의의 데이터(암호 등)를 고정된 길이의 데이터로 매핑하여 원래의 입력값과의 관계를 찾기 어렵게 만든 것
- SHA, MD5


