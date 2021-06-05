import React, { useState } from "react";
import axios from "axios";
import ModalLabel from "components/atoms/ModalLabel";
import UploadModalTitleInput from "components/atoms/UploadModalTitleInput";
import UploadModalDescInput from "components/atoms/UploadModalDescInput";
import UploadModalFileInput from "components/atoms/UploadModalFileInput";
import UploadModalBtn from "components/atoms/UploadModalBtn";
import * as S from "./style";

export interface UploadModalProps {
  text: string;
}

const UploadModal: React.FC<UploadModalProps> = (): JSX.Element => {
  const [videoTitle, setVideoTitle] = useState("");
  const [videoDescription, setVideoDescription] = useState("");
  const [videoFile, setVideoFile] = useState(Object);

  const stateInitialize = () => {
    setVideoTitle("");
    setVideoDescription("");
    setVideoFile(Object);
  };

  const onSubmit = async (e: any) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("title", videoTitle);
    formData.append("description", videoDescription);
    formData.append("videoFile", videoFile);
    formData.append("processMethod", "null");

    const url = "http://localhost:8000/api/v1/deeps/";
    console.log(formData);
    try {
      await axios.post(url, formData, {
        headers: {
          "content-type": "multipart/form-data",
        },
      });
      stateInitialize();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <S.Container>
      <S.UploadModal onSubmit={onSubmit}>
        <S.UploadModalHeader>
          <ModalLabel text="비속어 필터링 하기" />
        </S.UploadModalHeader>
        <S.UploadModalContent>
          <S.UploadModalContentElement>
            <UploadModalTitleInput />
          </S.UploadModalContentElement>
          <S.UploadModalContentElement>
            <UploadModalDescInput />
          </S.UploadModalContentElement>
          <S.UploadModalContentElement>
            <UploadModalFileInput />
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
