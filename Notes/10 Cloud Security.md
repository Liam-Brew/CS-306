# Lecture 10: Cloud Security

## Cloud Computing

Outsourcing storage, computation, databases, analytics...

What is cloud computing?

- **on-demand self service**: add or subtract resources as necessary
- **broad network access**: mobile, desktop, mainframe
- **resource pooling**: multiple tenants share resources that can be reassigned dynamically according to need and invisibly to the tenants
- **rapid elasticity**: services can quickly and automatically scale up or down to meet customer need
- **measure service**: like water or gas, usage can be monitored for billing

On-demand self-service computing

- **Software as a service (SaaS)**: the cloud provider gives the customer access to applications running in the cloud
- **Platform as a service (PaaS)**: the customer has his or her own applications, but the cloud provides the languages and tools for creating and running them
  - ex: Azure or AWS
- **Infrastructure as a service (IaaS)**: the cloud provider offers processing, storage, networks, and other computing resources that enable customers to run any kind of software
  - renting computing power (ex: Amazon's EC2 or S3), essentially renting a hash table

### Deployment Models

- **private cloud**: infrastructure that is operated exclusively by and for the organization that owns it
- **community cloud**: shared by several organizations with common needs, interests, or goals
- **public cloud**: owned by a cloud service provider and offered to the general public
- **hybrid cloud**: composed of two or more types of clouds, connected by technology that enables data and applications to balance loads among those clouds

### Security Benefits of Cloud Services

- **geographic diversity**: many cloud providers run data centers in disparate geographic locations and mirror data across locations, providing protection from natural and other local disasters
- **platform and infrastructure diversity**: different platforms and infrastructures mean different bugs and vulnerabilities, which make a single attack or error less likely to bring a system down
  - using cloud services as part of a larger system can be a good way to diversify your technology stack (e.g., Honeywords, virtualization etc.)

Cloud-based security functions:

- email filtering
- DDoS protection
- Network monitoring

## Authentication

Salting does not elminiate dictionary attacks: it just makes it user-specific, thereby slowing them down. Only after the compromise of a server (gaining the salt) and learning the user's name can the attacker begin a user-specific dictionary attack, which can not be repeated for other users.
