console.log(__dirname + `/build/models/*`);

export default {
  type: process.env.DB_TYPE,
  host: process.env.DB_HOST,
  port: 3306,
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE,
  synchronize: true,
  logging: false,
  entities: [__dirname + `/src/models/*.ts`, __dirname + `/build/models/*.js`],
  migrations: [__dirname + `/build/models/migration/**/*`],
  subscribers: [__dirname + `/build/models/subscriber/**/*`],
  cli: {
    entitiesDir: `build/models/`,
    migrationsDir: `build/models/migration`,
    subscribersDir: `build/models/subscriber`,
  },
};
