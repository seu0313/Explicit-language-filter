import express from "express";
import deepRouter from "./deep.router";

const router = express.Router();

router.use("/deeps", deepRouter);

export default router;
