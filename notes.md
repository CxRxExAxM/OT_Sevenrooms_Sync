# Project Notes Etc.


## Links
### OpenTable API Documentation
https://docs.opentable.com/

### SevenRooms API Documentation

### Postman API Interface
https://mike-6155807.postman.co/



# Webhook vs. API Polling
Webhooks and polling are two methods for applications to receive updates from each other, but they differ in how they initiate the communication: webhooks are push-based (server sends notifications), while polling is pull-based (client requests updates). [1, 2, 3]  
Here's a more detailed comparison: 
Polling (Pull-Based): [2, 3]  

• How it works: The client (application requesting updates) periodically checks the server for new data or events. [2, 3]  
• Initiation: Client-initiated (client makes the request). [1, 2]  
• Real-time updates: Not ideal for real-time updates, as the client needs to wait for the polling interval to check for updates. [2, 3]  
• Resource usage: Can be resource-intensive, as the client makes frequent requests even if there are no updates. [2, 3]  
• Simplicity: Simpler to implement than webhooks, as it requires less setup on the server-side. [2, 3]  
• When to use: Suitable for applications where updates are infrequent or when the client needs more control over when to check for updates. [2, 3]  

Webhooks (Push-Based): [1, 2]  

• How it works: The server sends a notification to the client when a specific event occurs, without the client having to request it. [1, 2]  
• Initiation: Server-initiated (server sends the notification). [1, 2]  
• Real-time updates: Better for real-time updates, as the client is notified immediately when an event occurs. [2, 4]  
• Resource usage: More efficient in terms of resource usage, as the server only sends notifications when there are updates. [2, 4]  
• Simplicity: Can be more complex to implement than polling, as it requires more setup on the server-side. [2, 3]  
• When to use: Suitable for applications that require real-time updates, such as social media feeds or online gaming. [2, 4]  

Here's a table summarizing the key differences: [2, 3]  

| Feature | Polling | Webhooks  |
| --- | --- | --- |
| Communication Type | Pull-based (client requests data) | Push-based (server sends notifications)  |
| Initiation | Client-initiated | Server-initiated  |
| Real-time updates | Not ideal | Better  |
| Resource usage | Can be resource-intensive | More efficient  |
| Complexity | Simpler to implement | Can be more complex  |
| Use Cases | Infrequent updates, client control | Real-time updates, event-driven applications  |

Generative AI is experimental.

[1] https://www.svix.com/resources/faq/webhooks-vs-api-polling/[2] https://blog.bytebytego.com/p/ep100-polling-vs-webhooks[3] https://www.linkedin.com/pulse/comparison-between-polling-webhooks-world-apis-abdelilah-el-attari-[4] https://medium.com/@reetesh043/polling-vs-webhooks-4723883a6b40


