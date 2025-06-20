# domainTakeOverReport
Tool created to check .gov.in websites incase of their domain take over

# Flow of Program
1. Pull hyperlinks based on google dork queries
2. Open the hyperlink, get headers and check for redirection
3. If redirection to a betting,porn or any other non-government site, flag it as critical
4. If headers have problematic headers, such as Sec-Fetch-Site being set to Cross-Site, then flag it as medium
