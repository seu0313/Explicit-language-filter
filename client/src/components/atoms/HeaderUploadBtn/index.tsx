import React from "react";
import * as S from "./style";

export interface HeaderUploadBtnProps {
  src?: string;
  isUploadClicked: boolean;
  setIsUploadClicked: (value: boolean) => void;
}

const HeaderUploadBtn: React.FC<HeaderUploadBtnProps> = ({
  src,
  isUploadClicked,
  setIsUploadClicked,
}): JSX.Element => {
  const onClick = (): void => {
    setIsUploadClicked(!isUploadClicked);
  };
  return <S.HeaderUploadBtn src={src} onClick={onClick} />;
};

export default HeaderUploadBtn;
