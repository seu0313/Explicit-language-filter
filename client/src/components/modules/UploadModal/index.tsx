import React, { useState } from "react";
import axios from "axios";
import Label from "components/atoms/Label";
import UploadModalTitleInput from "components/atoms/UploadModalTitleInput";
import UploadModalDescInput from "components/atoms/UploadModalDescInput";
import UploadModalFileInput from "components/atoms/UploadModalFileInput";
import UploadModalBtn from "components/atoms/Button";
import * as S from "./style";

export interface UploadModalProps {
  isUploadClicked: boolean;
  setIsUploadClicked: (value: boolean) => void;
}

const UploadModal: React.FC<UploadModalProps> = ({
  isUploadClicked,
  setIsUploadClicked,
}): JSX.Element => {
  const [videoTitle, setVideoTitle] = useState("");
  const [videoDescription, setVideoDescription] = useState("");
  const [videoFile, setVideoFile] = useState(Object);

  const stateInitialize = () => {
    setVideoTitle("");
    setVideoDescription("");
    setVideoFile(Object);
  };

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
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
      stateInitialize();
      setIsUploadClicked(!isUploadClicked);
    } catch (error) {
      console.log(error);
    }
  };

  const handleVideoTitleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setVideoTitle(e.currentTarget.value);
  };
  const handleVideoDescriptionChange = (
    e: React.ChangeEvent<HTMLInputElement>,
  ) => {
    setVideoDescription(e.currentTarget.value);
  };
  const handleVideoFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.currentTarget.files;
    if (!file) return;
    setVideoFile(file[0]);
  };

  return (
    <S.Container>
      <S.UploadModal method="POST" action="/" onSubmit={onSubmit}>
        <S.UploadModalHeader>
          <Label type="text" width="165px" text="비속어 필터링 하기" />
        </S.UploadModalHeader>
        <S.UploadModalContent>
          <S.UploadModalContentElement>
            <UploadModalTitleInput onChange={handleVideoTitleChange} />
          </S.UploadModalContentElement>
          <S.UploadModalContentElement>
            <UploadModalDescInput onChange={handleVideoDescriptionChange} />
          </S.UploadModalContentElement>
          <S.UploadModalContentElement>
            <UploadModalFileInput onChange={handleVideoFileChange} />
          </S.UploadModalContentElement>
        </S.UploadModalContent>
        <S.UploadModalFooter>
          <UploadModalBtn />
        </S.UploadModalFooter>
      </S.UploadModal>
    </S.Container>
  );
};

export default UploadModal;
