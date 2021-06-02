import { NextFunction, Request, Response } from "express";
import { resError, resJSON, resMSG } from "@utils/module";

export const errorNotFound = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const error = new resError(404, resMSG.NOT_FOUND);
  next(error);
};
export const errorHandler = (
  err: resError,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const status = err.status || 500;
  const message = err.message || resMSG.INTERNAL_SERVER_ERROR;
  const data = err.data;

  res.status(status).json(resJSON(false, message, data));
};
