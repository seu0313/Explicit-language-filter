import React from "react";
import * as S from "./style";

export interface HeaderUploadBtnProps {
  src: string;
  isUploadClicked: boolean;
  setUploadClicked: (value: boolean) => void;
}

const HeaderUploadBtn: React.FC<HeaderUploadBtnProps> = ({
  src,
  isUploadClicked,
  setUploadClicked,
}): JSX.Element => {
  const onClickUploadBtn = (): void => {
    setUploadClicked(!isUploadClicked);
  };
  return (
    <S.Container>
      <S.HeaderUploadBtn src={src} onClick={onClickUploadBtn} />
    </S.Container>
  );
};

export default HeaderUploadBtn;
