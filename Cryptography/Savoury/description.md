## Description

Can salt be black? I'm not sure, but **pepper** surely is.  

You are given 15 salted hashes and a list of 100 passwords, out of which any 15 were used to generate these hashes.  

Flag format:  
`DJSISACA{<triplet1>_<triplet2>_..._<triplet15>_<base_salt>}`  

where each `<tripletX>` is defined as:  

- first letter of password X  
- digit for X  
- suffix for X  
