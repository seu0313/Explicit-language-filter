import { Deep } from "@models/deep.model";
import { getRepository } from "typeorm";

export const findAllService = async () => {
  const result = await getRepository(Deep).find();
  console.log(result);
  return result;
};
export const findOneService = () => {};
export const createDeepService = () => {};
export const updateDeepService = () => {};
export const deleteDeepService = () => {};
