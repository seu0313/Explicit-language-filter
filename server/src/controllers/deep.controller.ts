import { Request, Response, NextFunction, request } from "express";
import * as deepService from "@services/deep.service";
import { serverURL } from "../config/index";
import { resError, resJSON, resMSG } from "@utils/module";

export const findAllController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const result = await deepService.findAllService();
  res.status(200).json(resJSON(true, resMSG.OK, result));
};
export const findOneController = (
  req: Request,
  res: Response,
  next: NextFunction
) => {};
export const createDeepController = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  console.log(req.file);
  console.log(
    resJSON(true, resMSG.OK, `${serverURL}/media/${req.file["path"]}`)
  );
  res
    .status(200)
    .json(resJSON(true, resMSG.OK, `${serverURL}/media/${req.file["path"]}`));
};
export const updateDeepController = (
  req: Request,
  res: Response,
  next: NextFunction
) => {};
export const deleteDeepController = (
  req: Request,
  res: Response,
  next: NextFunction
) => {};
