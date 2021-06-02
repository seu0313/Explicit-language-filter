import express from "express";
import path from "path";
import multer from "multer";
import * as deepController from "@controllers/deep.controller";

/**
 * Classify user requests.
 *
 * @path api/v2/deeps/
 *
 * @author seu0313
 * @since 2.0.0
 */

// Perform downloaded image data processing with Multer
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");
  },
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname);
    cb(
      null,
      path.basename(file.originalname, ext) + new Date().valueOf() + ext
    );
  },
});
const upload = multer({ dest: "./uploads/", storage: storage });

// ----------------------------------------------------------------------

const router = express.Router();

router.get("/:id", deepController.findOneController);
router.patch("/:id", deepController.updateDeepController);
router.delete("/:id", deepController.deleteDeepController);
router.post(
  "/",
  upload.single("videoFile"),
  deepController.createDeepController
);
router.get("/", deepController.findAllController);

export default router;
