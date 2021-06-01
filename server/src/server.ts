import http from "http";
import app from "./config/app";
import { env, port } from "./config/index";
import { createConnection, getConnection } from "typeorm";

const runServer = async () => {
  if (env === "test") return;

  const server = app.listen(port, () => {
    console.clear();
    console.log(`
      \x1b[32mCompiled successfully!\x1b[0m\n
      You can now use \x1b[34mserver\x1b[0m.\n
      \t\x1b[1mLocal:\x1b[0m \t\thttp://localhost:\x1b[1m${port}\x1b[0m/api/v1`);
  });
  try {
    await createConnection();
    console.log(`
      \t\x1b[1mDB Status:\x1b[0m database connected
      \t\x1b[1mDB Type:\x1b[0m ${process.env.DB_TYPE}\n
      Note that the development build is not optimized.
      To create a production build, use \x1b[36myarn build\x1b[0m.
    `);
  } catch (err) {
    stopServer(server, err);
  }
};

const stopServer = async (server: http.Server, err?: any) => {
  const connection = getConnection();
  await connection.close();

  server.close();
  process.exit();
};

runServer();
