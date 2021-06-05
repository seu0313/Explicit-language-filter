import React from "react";
import * as S from "./style";

const UploadModalDescInput: React.FC = (): JSX.Element => {
  return (
    <S.Container>
      <S.UploadModalDescInput type="text" placeholder="설명을 입력해주세요*" />
    </S.Container>
  );
};

export default UploadModalDescInput;
