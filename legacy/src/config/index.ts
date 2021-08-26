import dotenv from "dotenv";
dotenv.config();

export const env = process.env.NODE_ENV || "development";
export const port = process.env.PORT || 4000;
export const morganType = env === "production" ? "combined" : "dev";
export const clientURL =
  env === "production"
    ? process.env.CLIENT_URL_PRODUCTION
    : process.env.CLIENT_URL_DEVELOPMENT;
export const serverURL =
  env === "production"
    ? process.env.SERVER_URL_PRODUCTION
    : process.env.SERVER_URL_DEVELOPMENT;
