import { Deep } from "@models/deep.model";
import path from "path";
import childProcess from "child_process";
import ThumnailGenerator from "video-thumbnail-generator";
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
  const BASE_ROOT = path.dirname(path.dirname(__dirname));
  const UPLOADS = path.join(BASE_ROOT, "uploads");

  const tg = new ThumnailGenerator({
    sourcePath: `${UPLOADS}/${reqFile["filename"]}`,
    thumbnailPath: `${UPLOADS}/thumb/`,
  });

  const thumbnail = await tg.generateOneByPercent(50);
  console.log(thumbnail);

  const { title, description, processMethod } = reqBody;
  const deepRecord = getRepository(Deep).create({
    title,
    description,
    processMethod,
    videoFile: `${serverURL}/uploads/${reqFile["filename"]}`,
    src: `${serverURL}/uploads/thumb/${thumbnail}`,
  });
  const result = await getRepository(Deep).save(deepRecord);
  return result;
};

export const getDeepFromPython = async () => {
  const result = childProcess.spawn("python", [
    "/Users/lingo/Desktop/Bad-word-filter/server/src/services/python.py",
  ]);
  console.log("실행");

  result.stdout.on("data", (data) => {
    console.log(data.toString());
  });
  console.log("실행2");
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
