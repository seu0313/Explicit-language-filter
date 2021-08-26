import express from "express";
import deepRouter from "./deep.router";
import { getDeepFromPython } from "@services/deep.service";

const router = express.Router();

router.use("/deeps", deepRouter);
router.use("/test", async (req, res, next) => {
  await getDeepFromPython();

  next();
});

export default router;
