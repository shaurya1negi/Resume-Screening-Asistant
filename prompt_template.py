prompt_template = """"
Categorize the following  resume content into one of the following categories only :- Data Science, Software
Development, HR .\n
resume content:- 
Summary:
Software Developer specializing in security and encryption.\n
Skills:
Java, Python, C ,Network Security, Cryptography, Penetration Testing\n
Professional Experience:
Security Software Developer | SafeGuard | 2022·2025 ,Developed encryption libraries for secure messaging apps.Conducted vulnerability assessments.Intern | SecureIT | 2021·2022l Automated security audits.\n
Answer:Software Development

passed resume content:- 
Summary:
%s\n
Skills:
%s\n 
Professional Experience:
%s\n
Answer:
"""   


