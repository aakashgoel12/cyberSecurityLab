# Task: Prepare a threat modeling for the below manufacturing plant scenario. Identify and tabulate the risks, rate the impact and provide remediation guidelines.

## Objective: Understand and analyze threats to your system designs in its early stage.

## Tool: MS Threat Modelling

## Download Link: MS Threat Modelling Tool (https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool)

## Content
- Exercise -- Website accessed by Database
    - Database
    - Web Application
    - Web application making request to Database
    - Database sending response to web application
    - check threats
    - click on views on top and select analysis view, 

- Exercise -- The Organization is planning to upgrade its existing OT (Operational Technology) infrastructure. Part of the upgrade strategy involves leveraging cloud-based services to control the systems. The objective of this upgrade is to send values from temperature sensors in the OT network to IT cloud services through a secure communication channel and control the actuator based on algorithms executed in the cloud service.

**Architecture Flow Diagram:**
The architecture flow diagram should illustrate the flow of data from the temperature sensors in the OT network to the cloud services and back to the actuators. Here is a textual description of the diagram:

1. Temperature Sensors (OT Network):
    - Collect temperature data from various points in the manufacturing plant.
2. Secure Communication Channel:
    - Transmit the collected data securely to the cloud services.
3. Cloud Services (IT Network):
    - Receive the temperature data.
    - Process the data using algorithms to determine necessary actions.
4. Actuators (OT Network):
    - Receive control commands from the cloud services.
    - Adjust operations based on the received commands.


** References**
- https://github.com/hysnsec/awesome-threat-modelling
- https://github.com/domssilva/ThreatModeling