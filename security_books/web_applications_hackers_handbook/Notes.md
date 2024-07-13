# The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws

### Table of Contents

- [Ch 1: Web Application (In)security](#ch-1-web-application-insecurity)
- [Ch 2: Core Defense Mechanisms](#ch-2-core-defense-mechanisms)
- [Ch 3: Web Applications Technologies](#ch-3-web-application-technologies)
- [Ch 4: Mapping The Application](#ch-4-mapping-the-application)
- [Ch 5: Bypassing Client-Side Controls](#ch-5-bypassing-client-side-controls)
- [Ch 6: Attacking Authentication](#ch-6-attacking-authentication)
- [src](#https://samsclass.info/129S/129S_S20.shtml#lecture)

# Ch 1: Web Application (In)security

<br>

# Ch 2: Core Defense Mechanisms

- simple little operations like logging out , you should think about what they should do and what they really do !!
- post method in HTTP Protocol sends data below the request , and usually used with operations when u want to do action Once , like Buying a product
- Typical URL (uniform resource locator) :
  - protocol://hostname[:port]/[path/]file[?param=value]

# Ch 3: Web Application Technologies

- HTTP Parameteres

  - May be sent in one of these ways :

    - In the url query string
    - In the file path of REST-style URLs
    - In HTTP cookies (mos common)
    - In the body of requests using the POST method

  - Other Inputs :
    - Server-side application may use any part of the HTTP request as an input
      - Such as User-Agent

- SOAP

  - if user-supplied data is incorporated into SOAP requests, it can have code injection vulnerabilities (just like stored XSS `"><script>alert(1)</script>`)
  - Server usually publishes available services and parameters using Web Services Description Language(WSDL)
  - soapUI and other tools can generate requests based on WSDL file

- Same-Origin Policy

  - Prevents content from different origins interfering with each other in a browser
  - Content from one website can only read and modify data from the same website
    - Ex: scripts on Facebook can't read or write to data on ur online banking page
  - When this process fails, you get XSS,CSRF and other attacks

- State and Sessions

  - Stateful data required to supplement stateless HTTP
  - This data is held in a server-side structure called a session
  - The session contains data such as items added to a shopping cart
  - some state data is stored on the client, often HTTPS HTTP cookies or hidden from fields

- URL Encoding

  - URLs may contain only printable ASCII characters
    - 0x20 to 0x7e, icnlusive
  - TO transfer other characters, problematic ASCII characters, over HTTP, they must be URL-encided

- Unicode Encoding

  - Supports all the world's writing systems
  - 16 bits per character, starting with %u

- URF-8 Encoding

  - Variable length for a char
  - Users % character before each byte
  - Unicode and UTF-8 are often used to bypass filters in attacks

- HTML Encoding
  - HTML encoding defines numerous HTML entities to represent specific literal characters
    - `&lt;` -> <
- Base64 Encoding

  - originally designed to send images through emails
  - represents binary data using 64 ASCII characters
    - six bits at a time
  - character set :
    [A-Z],[a-z],[1-9],[+,/]
  - Bitcoin addresses are base 58

- Hex Encoding
  - Hexadecimal numbers corresponding to each ASCII character
<!-- <br> -->

# Ch 4: Mapping The Application

- Robots.txt
  - intended to stop search engines from indexing these contents
  - may guide spiders to interesting content
  - and this probably tells u where the bad guy should look, this is apparently where the secrets are
  - u can install user agent switcher and change urselves into googlebot and then u'll see the content the way google does

- Discovering Hidden Content
  - Finding it requires automated testing, manual testing, and luck
  - Testing or debugging features left in application
  - Different functioanlity for different categories of users
    - Anonymous, authenticated, administrators
  - Backup copies of live files
    - may be non-executable and reveal source code
  - Backup archives that contain snapshot of entire application
  - New functionality impelmented for testing but not yet linked from main application
  - Default functionality in an off-the-shelf application that has been superficially hidden from the user but not removed
  - OLd versions of files-- may still be exploitable
  - Configuration and include files containing sensitive data such as database credentials
  - Source files from which application functions were compiled 
  - Commpents in source code; may contain usernames and passwords, "test this" marks, and other useful data
  - Log files--may contain valid usernames , session tokens, etc.

  - ```skipfish``` google's phone scanner , good tool

- More Clues
  - Search for temporary files created by tools and file editors
  - .DS_Store file (a directory index created by Mac OS X)
  - file.php-1 created when file.php is edited
  - .tmp files created by many tools
- Public Information
  - search engines (and cached content)
  - Google Dorks

- Discovering Hidden Parameters
  - Try adding "debug=true" to requests
  - Or test, hide, source, etc.
  - Burp intruder can do this

- Analyzing the application
  - Key areas
    - Core functionality
    - Peripheral behavior: off-site links, error messages, administrative and logging functions, and use of redirects
    - Core security mechanisms:
      - session state, access control, authentication
      - user registration, password change, account recovery
    - Everywhere the application processes user-supplied input
      - URL , query strin, POST data, cookies
    - Client-side technologies
      - Forms, scripts,thick-client components (Java applets,ActiveX controls, and Flash), and cookies
    - Server-side technologies
      - Static and dynamic pages, requests parameters, SSL,Web server software, interaction with databbases, email systems, and other back-end components

- Entry Points for User Input
  - Every URL string up to the query string marker
  - Every parameters submitted within the URL query string
  - Every parameter submitted within the body of a POST request
  - Every cookie
  - Every other HTTP header that the application might process-- 
    - In particular, the User-Agent, Referer, Accept,Accept-Language, and Host headers

- HTTP Headers
  - User-Agent is used to detect small screens 
    - Sometimes to modify content to boost search engine rankings
    - May allow XSS and other injection attacks
  - Changing User-Agent may reveal a different user interface
  - Applications behind a load balancer or proxy may user X-Forwarded-For header to identify the source
  - Can be manipulated by attacker to inject contet

- Out-Of-Band Channels
  - User data may come in via
    - Email
    - Publishing content via HTTP from another server (e.g. WebDAV)
    - IDS that sniffs traffic and outs it into a web application
    - API interface for non-browser user agents, such as cell phone apps, and then shares data with the primary web applcation
<br>

- IDS may put data sniffed from network packets into a web app

# Ch 5: Bypassing Client-Side Controls

- the user can bypass any client side validation using proxies such as burb or zap
- scenarios and applcation of it:
  - the user could modify the price of product that located in the body of the POST request
  - the user could modify any data passed with the cookie
  - the user might change the referrer header
  - the user might bypass length limited fields (limited by javascript) or any validation used by javascript
  - the user might modify the response from the server and removes all the client side validation , enable disabled fields , show hidden fields and so on
- fact : ```you can't trust anything from a client and can't really assume that anything you put on the server really made it to the client , they could have modified the data coming in too  so you hvae to think in the suspicious way to make things secure```
- accept-encoding header:
  - if u have asked for a big page it would come in gzip format , the fun thing if u have droped this header u could take it in clear txt and modify it as u want 

#### Handling Opaque Data

- If you know the plaintext, you may be able to deduce the obfuscation algorithm
- App may contain functions elsewhere that you can leverage to obfuscate plaintext you control
- you can replay opaque text without deciphering it
- Attack server-side logic with malformed strings, such as overlong values, different charecter sets, etc .

#### Sending and recieving data from the client side

- you can encrypt something, this protects it from unauthorized viewing
<br>
or 
<br>
- you can sign it, this means it's not a secret (still can be figured out) it's just means you can tell if it's benn modified, and all u really care about here probably is a signature you don't really need to encrypt it you just need the signature so u know if it's been modified

<br>

- Use shift + refresh to enforce full reload

#### Tips

- Where JavaScript is used for input validation
- Submit data would have failed validation
  - Using a proxy, or with modified source code
- Determine whether validation is also performed on the server
- if multiple fields are validated, enter valid data in all fields except one at a time , to test all the cases

#### Proper Use of Client side validation

- Client-side validation can improve performance and user experience
- Faster response and no wasted server time on invalid entries
- But the validation cannot be trusted and must be repeated on the server

#### Add Prameter in Burp
 - check the prameter section in the repeater and press the add button to insert the disabled field
 - it may still be used on the server-side

#### Handling Client-Side Data Securely

- Don't sned critical data like prices from the client
  -instead send the product ID and grap the price form the DB , therefore even if the user manpulated the ID Of the product it will still pay the right amount of money
- If you must send important data, sign and/or encrypt it to avoid user tampering
  - May be vulnerable to replay or cryptographic attacks

#### Validating Client-Generated Data

- All client-side validation methods are vulnerable
  - They may be useful for performance, but they can never be trusted
- The only secure way to validate data is on the server

#### Logs and Alerts

- Server-Side intrusion detection defenses should be aware of client-side validation
- It should detect invalid data as probably malicious, triggering alerts and log entries
- May terminate user's session, or suspend user's account

<br>


# Ch 6: Attacking Authentication

<br>

#### Authentication Technologies

- HTML forms-based authentication
- Multifactor mechanisms, such as those combining passwords and physical tokens
- Client SSL certificates and/or smart cards
- HTTP basic and digest authentication
- Windows-integrated authentication using NTLM or Kerberos
- Authentication services

#### HTTP Authentication

- Basic, Digest, and Windows-integrated
- Rarely used on the internet
- More common in intranets, especially windows domains
  - So authenticated employees can easily access secured resources

#### Username Importance

- Attacks that reveal valid usernames are called "username enumeration"
- Not as bad as finding a password, but still a privacy intrusion
- But could be used for social engineering attacks, such as spearphishing emails
<br>

#### HTTP Risks

- If credentials are sent unencrypted , the eavesropper's task is trivial, but even HTTPS can't prevent theses risks:
  - Credentials sent in the query string are likely to appear in server logs, browwser history, and logs of reverse proxies
  - Many sites take credentials from a POST and then redirect it (302) to another page with credentials in the query string
- Cookie risks:
  - Web apps may store credentials in cookies
  - Even if cookies cannhot be decrypted, they can be re-used
- Many pages open a login page via HTTP and use an HTTPS request in the form
  - This can be defeated by man-in-the-middle attack, like sslstrip  


<br>

- IMEI number : like MAC address , it's a number in each phone uniquely identifies the phone

#### Handling Credentials

- Password hashes must be salted and stretched 
- Salt: add random bytes to the password before hashing it
- Stretched: many rounds of hashing  

(this from me dedoxd2: Django do 720,0000 rounds of hashing passwords before saving it)
## Cool Quotes

    - all the security relies on knowing who you are talking to
