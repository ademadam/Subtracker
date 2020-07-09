## Subtracker


Is automating python script that help to keep traking new added/discovered subdomains using well known tools (at the mean time only sublister)

## What this tool do 
1. brute force domains of single one using other tools (sublister)
2. Put the first results in `1.txt`
3. Now it will re-do the above steps but add the ruslts into `2.txt`
4. Now it will compare the domains that are included in `2.txt` and not existed in`1.txt` (new subdomains)
5. Noww it will make a post request with the found domain to your host (the 2nd argument given)


## How to use
```
python subtracker target.com logger.com
```

1. this will make subdomain bruteforcing of `target.com`and will put the results to `logger.com`.


## To Do :
Right now i've added the core , i'm developing it to :
1. Make the brute for each 5 minutes , (now it will re-do the brute forcing whenever you execute it)
2. Make it post domain name/ip/time found & Make a Well and Better UX that will receive the domain name/ip/time found at
3. Add more tools (amass, findomain specially)
