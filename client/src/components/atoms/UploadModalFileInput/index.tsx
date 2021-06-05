import React from "react";
import * as S from "./style";

const UploadModalFileInput: React.FC = (): JSX.Element => {
  return (
    <S.Container>
      <S.UploadModalFileInput
        type="file"
        accept="video/mp4, video/avi, video/mov"
      />
    </S.Container>
  );
};

export default UploadModalFileInput;
