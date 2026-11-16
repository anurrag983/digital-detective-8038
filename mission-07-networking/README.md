# Mission 7 — How computers communicate

## 1. Task / objective
Learn basic computer networking terms, test internet reachability using `ping` and `nslookup`, and understand what happens when a web page opens.

## 2. Work completed
- Filled out the network concepts table with simple explanations.
- Tested `ping` and `nslookup` on my Mac.
- Wrote down the step-by-step process of opening a website in a browser.

## 3. Commands / tools used
- `ping -c 3 example.com`
- `nslookup example.com`

## 4. My understanding

### Task 7.1 — Network concepts
| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A small network in one room, home, or office building. | My home Wi-Fi connecting my Mac and phone. |
| **MAN** | A bigger network covering an entire city or large college campus. | A university network connecting different campus buildings. |
| **WAN** | A massive network that spans across cities, countries, and continents. | The global Internet. |
| **DNS** | The phonebook of the internet; converts website names into IP addresses. | Translating `google.com` into `142.250.x.x`. |
| **Router** | A box that directs internet traffic to the right device. | The home Wi-Fi router. |
| **Protocol** | Standard rules that devices must follow to talk to each other. | HTTP, HTTPS, TCP, IP. |
| **Packet switching** | Splitting data into small chunks (packets) to send them over the internet. | Streaming a YouTube video in packets. |
| **Client-server** | When one device (client) asks for data and another device (server) provides it. | My browser asking YouTube's server for a video. |

### Task 7.2 — Testing network commands
- **Connectivity test (`ping -c 3 example.com`):** Sent 3 test packets. All 3 returned with 0.0% packet loss and around 4.8ms response time. This proves my internet is working and can reach that server.
- **DNS lookup (`nslookup example.com`):** Showed the IP addresses `104.20.23.154` and `172.66.147.243`.
- **Why DNS is needed:** We cannot memorize long numbers for every website we visit. DNS lets us type words like `example.com`, and immediately finds the right server number behind the scenes.

### Task 7.3 — What happens when you open a website (7 Steps)
1. I type `https://example.com` into my browser and hit Enter.
2. The browser contacts a DNS server to find the IP address for `example.com`.
3. The DNS server replies back with the numeric IP address (`172.66.147.243`).
4. My computer opens a secure connection (TCP + HTTPS) to that IP address through my home router.
5. The browser sends an HTTP request asking for the web page content.
6. The web server at that address processes the request and sends the page files (HTML, CSS, images) back in data packets.
7. My browser puts the packets together and renders the webpage on my screen.

## 5. Difficulties faced
When I first ran `ping example.com`, it kept running without stopping.

## 6. How I resolved them
I pressed `Ctrl + C` to stop it, and then learned to use `ping -c 3 example.com` to only send 3 packets.

## 7. Evidence / files
- Network observations recorded above.

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
