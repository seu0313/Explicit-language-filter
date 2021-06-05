import React from "react";
import * as S from "./style";

export interface UploadModalDescInputProps {
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const UploadModalDescInput: React.FC<UploadModalDescInputProps> = ({
  onChange,
}): JSX.Element => {
  return (
    <S.Container>
      <S.UploadModalDescInput
        type="text"
        placeholder="설명을 입력해주세요*"
        onChange={onChange}
      />
    </S.Container>
  );
};

export default UploadModalDescInput;
