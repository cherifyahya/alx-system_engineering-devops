# Service Outage Postmortem

## Issue Summary
- **Duration:** The outage occurred from March 8, 2024, at 10:00 AM (UTC) to March 8, 2024, at 2:00 PM (UTC), lasting for a total of four hours.
- **Impact:** The outage affected our cloud-based storage service, resulting in complete unavailability of stored data for all users. Approximately 80% of our user base experienced disruption in accessing their files, leading to significant productivity loss and frustration.
- **Root Cause:** The root cause of the outage was identified as a hardware malfunction in a critical network switch, causing a cascading failure in the network infrastructure.

## Timeline
- 10:00 AM (UTC): Incident detected by monitoring systems due to a spike in error rates and latency.
- 10:05 AM (UTC): Engineers alerted and investigation initiated.
- 10:15 AM (UTC): Root cause identified as a malfunction in the core networking equipment.
- 10:30 AM (UTC): Mitigation measures deployed to reroute traffic and isolate affected components.
- 2:00 PM (UTC): Service fully restored after repairs and validation.

## Root Cause and Resolution
- **Root Cause Explanation:** A critical hardware malfunction occurred in a network switch, leading to a cascading failure in the network infrastructure. This resulted in congestion and loss of connectivity between servers and storage nodes.
- **Resolution:** The issue was resolved through extensive repairs to the malfunctioning network switch and the implementation of redundant networking components. Additionally, capacity planning measures were undertaken to prevent congestion during peak usage periods.

# Corrective and Preventative Measures
