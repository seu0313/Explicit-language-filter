import express from "express";
import multer from "multer";
import * as deepController from "@controllers/deep.controller";

const router = express.Router();
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});
const upload = multer({ dest: "./uploads/", storage: storage });

router.get("/:id", deepController.findOneController);
router.patch("/:id", deepController.updateDeepController);
router.delete("/:id", deepController.deleteDeepController);
router.post(
  "/",
  upload.single("video_file"),
  deepController.createDeepController
);
router.get("/", deepController.findAllController);

export default router;
