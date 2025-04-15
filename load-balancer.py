
# Request comes in...

servers = {
    'server1': '0.0.0.0:3000',
    'server2': '0.0.0.0:3001',
}

nextServer = Math.round(Math.random()) // ==> 0,1

connectedServer = connect(nextServer);

# Request is routed to connectedServer


"""Load Balancer Algorithms
 * Least connection
 * Weighted least connection
 * Resource-based
 * Weighted response time
 * Round robin
 * Weighted round robin
 * IP Hash

 https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/
""" 