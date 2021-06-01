import { Deep } from "@models/deep.model";
import { getRepository } from "typeorm";

export const findAllService = async () => {
  const result = await getRepository(Deep).find();
  console.log(result);
  return result;
};
export const findOneService = async () => {};
export const createDeepService = async () => {};
export const updateDeepService = async () => {};
export const deleteDeepService = async () => {};
