import React from "react";
import * as S from "./style";

export interface UploadModalFileInputProps {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const UploadModalFileInput: React.FC<UploadModalFileInputProps> = ({
  onChange,
}): JSX.Element => {
  return (
    <S.Container>
      <S.UploadModalFileInput
        type="file"
        accept="video/mp4, video/avi, video/mov"
        onChange={onChange}
      />
    </S.Container>
  );
};

export default UploadModalFileInput;
