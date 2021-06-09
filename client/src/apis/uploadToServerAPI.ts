import axios from "axios";

interface FormPrps {
  videoTitle: string;
  videoDescription: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  videoFile: any;
}

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export const uploadToServerAPI = async ({
  videoTitle,
  videoDescription,
  videoFile,
}: FormPrps) => {
  const url = "http://localhost:8000/api/v1/deeps/";

  const formData = new FormData();
  formData.append("title", videoTitle);
  formData.append("description", videoDescription);
  formData.append("videoFile", videoFile);

  try {
    await axios.post(url, formData, {
      headers: {
        "content-type": "multipart/form-data",
      },
    });
  } catch (error) {
    // eslint-disable-next-line no-console
    console.log(error);
  }
};
