import React, { useState } from "react";
import Label from "components/atoms/Label";
import Input from "components/atoms/Input";
import UploadModalBtn from "components/atoms/Button";
import { uploadToServerAPI } from "lib/api/uploadToServerAPI";
import * as S from "./style";

export interface UploadModalProps {
  isUploadClicked: boolean;
  setIsUploadClicked: (value: boolean) => void;
  renderHandler: () => void;
}

const UploadModal: React.FC<UploadModalProps> = ({
  isUploadClicked,
  setIsUploadClicked,
  renderHandler,
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

    try {
      await uploadToServerAPI({ videoTitle, videoDescription, videoFile });
      stateInitialize();
      setIsUploadClicked(!isUploadClicked);
    } catch (error) {
      // eslint-disable-next-line no-console
      console.log(error);
    }

    renderHandler();
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
    <S.UploadModal method="POST" action="/" onSubmit={onSubmit}>
      <Label type="text" width="165px" text="비속어 필터링 하기" />
      <Input
        onChange={handleVideoTitleChange}
        placeholder="제목을 입력해주세요*"
      />
      <Input
        onChange={handleVideoDescriptionChange}
        placeholder="설명을 입력해주세요*"
      />
      <Input
        type="file"
        accept="video/mp4, video/avi, video/mov"
        onChange={handleVideoFileChange}
      />
      <UploadModalBtn />
    </S.UploadModal>
  );
};

export default UploadModal;
