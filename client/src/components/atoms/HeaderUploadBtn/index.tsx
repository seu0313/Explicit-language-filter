import React from "react";
import * as S from "./style";

export interface HeaderUploadBtnProps {
  src: string;
  isUploadClicked: boolean;
  setIsUploadClicked: (value: boolean) => void;
}

const HeaderUploadBtn: React.FC<HeaderUploadBtnProps> = ({
  src,
  isUploadClicked,
  setIsUploadClicked,
}): JSX.Element => {
  const onClickUploadBtn = (): void => {
    setIsUploadClicked(!isUploadClicked);
  };
  return (
    <S.Container>
      <S.HeaderUploadBtn src={src} onClick={onClickUploadBtn} />
    </S.Container>
  );
};

export default HeaderUploadBtn;
