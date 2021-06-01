import express from "express";
import * as deepController from "@controllers/deep.controller";

const router = express.Router();

router.get("/:id", deepController.findOneController);
router.patch("/:id", deepController.updateDeepController);
router.delete("/:id", deepController.deleteDeepController);
router.post("/", deepController.createDeepController);
router.get("/", deepController.findAllController);

export default router;
