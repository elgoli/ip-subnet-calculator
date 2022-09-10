# ip-subnet-calculator
This is an IPV4 subnet calculator, it receives an IPv4 address and subnetmask as inputs from user and calculates the following outputs:

- Network address
- Broadcast address
- Number of valid hosts per subnet
- Number of mask bits in CIDR notation
- Wildcard mask

## Application Guideline
Run application locally
``` 
make run
```

Run application on a docker container
``` 
make docker-image
make run-container
```