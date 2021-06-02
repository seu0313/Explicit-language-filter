import { Request, Response, NextFunction } from "express";
import * as deepService from "@services/deep.service";
import { resError, resJSON, resMSG } from "@utils/module";

/**
 * Perform the actions requested by the user.
 * Send responses in the form of JSON to data corresponding to user's request.
 *
 * @author seu0313
 * @since 2.0.0
 */

// Send all Deep data to JSON format
export const findAllController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const result = await deepService.findAllService();
    if (!result) {
      throw new resError(400, resMSG.BAD_REQUEST);
    }
    res.status(200).json(resJSON(true, resMSG.OK, result));
  } catch (err) {
    next(err);
  }
};

// Send one Deep data to JSON format
export const findOneController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const result = await deepService.findOneService(req.params.id);
    if (!result) {
      throw new resError(400, resMSG.BAD_REQUEST);
    }
    res.status(200).json(resJSON(true, resMSG.OK, result));
  } catch (err) {
    next(err);
  }
};

// Send create response to JSON format
export const createDeepController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const result = await deepService.createDeepService(req.body, req.file);
    if (!result) {
      throw new resError(400, resMSG.BAD_REQUEST);
    }
    res.status(200).json(resJSON(true, resMSG.OK, result));
  } catch (err) {
    next(err);
  }
};

// Send update response to JSON format
export const updateDeepController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const result = await deepService.updateDeepService(req.params.id, req.body);
    if (!result) {
      throw new resError(400, resMSG.BAD_REQUEST);
    }
    res.status(200).json(resJSON(true, resMSG.OK, result));
  } catch (err) {
    next(err);
  }
};

// Send delete response to JSON format
export const deleteDeepController = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const result = await deepService.deleteDeepService(req.params.id);
    if (!result) {
      throw new resError(400, resMSG.BAD_REQUEST);
    }
    res.status(200).json(resJSON(true, resMSG.OK, result));
  } catch (err) {
    next(err);
  }
};
