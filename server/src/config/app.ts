import "module-alias/register";
import "reflect-metadata";
import express from "express";
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
app.use(cors({ origin: clientURL }));

// router settings
app.use("/api/v1", router);
app.use("/media/", express.static("uploads"));

// error handlers
app.use(errorNotFound);
app.use(errorHandler);

export default app;
