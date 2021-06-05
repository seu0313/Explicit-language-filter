import "module-alias/register";
import "reflect-metadata";
import express, { Request } from "express";
import morgan from "morgan";
import cors from "cors";

import router from "@routes/index";
import { morganType, clientURL } from "./index";
import { errorNotFound, errorHandler } from "@utils/errorHandler";

const app = express();

// app middlewares settings
app.use(morgan(morganType));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(
  cors({
    origin: clientURL,
    methods: ["GET", "POST", "PATCH", "DELETE"],
    credentials: true,
  })
);

// cors 체크 모듈
const corsCheck = (req: Request, callback: any) => {
  let corsOptions;
  const acceptList: any[] = [
    // ... url list,
  ];
  if (acceptList.indexOf(req.header("Origin")) !== -1) {
    corsOptions = { origin: true };
  } else {
    corsOptions = { origin: false };
  }
  callback(null, corsOptions);
};

// router settings (will change to v2)
app.use("/api/v1", cors(corsCheck), router);
app.use("/uploads", express.static("uploads"));

// error handlers
app.use(errorNotFound);
app.use(errorHandler);

export default app;
