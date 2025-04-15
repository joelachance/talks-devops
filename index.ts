const server = Bun.serve({
  port: 80,
  fetch(req) {
    return new Response("Hello Minnestar!");
  },
});

console.log(`Listening on http://localhost:${server.port} ...`);