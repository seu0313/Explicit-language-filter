import React from "react";
import * as S from "./style";

export interface UploadModalTitleInputProps {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const UploadModalTitleInput: React.FC<UploadModalTitleInputProps> = ({
  onChange,
}): JSX.Element => {
  return (
    <S.Container>
      <S.UploadModalTitleInput
        type="text"
        placeholder="제목을 입력해주세요*"
        onChange={onChange}
      />
    </S.Container>
  );
};

export default UploadModalTitleInput;
