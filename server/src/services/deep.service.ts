import { Deep } from "@models/deep.model";
import { resError, resMSG } from "@utils/module";
import { getRepository } from "typeorm";
import { serverURL } from "../config/index";

/**
 * Service module related to deep learning processing.
 *
 * @author seu0313
 * @since 2.0.0
 */

// Returns all Deep data in the form of a list.
export const findAllService = async () => {
  const result = await getRepository(Deep).find();
  return result;
};

// Returns one Deep data in the form of a list.
export const findOneService = async (reqId: string) => {
  const result = await getRepository(Deep).findOne(reqId);
  return result;
};

// Generate Deep data.
export const createDeepService = async (reqBody: any, reqFile: any) => {
  const { title, description, processMethod } = reqBody;
  const deepRecord = getRepository(Deep).create({
    title,
    description,
    processMethod,
    videoFile: `${serverURL}/${reqFile["path"]}`,
  });
  const result = await getRepository(Deep).save(deepRecord);
  return result;
};

// Update Deep data.
export const updateDeepService = async (reqId: string, reqBody: any) => {
  const { title, description, processMethod } = reqBody;
  const deep = await getRepository(Deep).findOne(reqId);
  if (!deep) throw new resError(400, resMSG.BAD_REQUEST);

  const deepRecord = getRepository(Deep).merge(deep, reqBody);
  const result = await getRepository(Deep).save(deepRecord);
  return result;
};

// Delete Deep data.
export const deleteDeepService = async (reqId: string) => {
  const deep = await getRepository(Deep).findOne(reqId);
  if (!deep) throw new resError(400, resMSG.BAD_REQUEST);

  const result = await getRepository(Deep).delete(reqId);
  return result;
};
