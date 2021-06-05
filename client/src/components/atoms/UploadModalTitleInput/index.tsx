import React from "react";
import * as S from "./style";

const UploadModalTitleInput: React.FC = (): JSX.Element => {
  return (
    <S.Container>
      <S.UploadModalTitleInput type="text" placeholder="제목을 입력해주세요*" />
    </S.Container>
  );
};

export default UploadModalTitleInput;
