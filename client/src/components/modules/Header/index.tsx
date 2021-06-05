import React from "react";
import Label from "components/atoms/Label";
import HamburgerBtn from "components/atoms/HamburgerBtn";
import HeaderUploadBtn from "components/atoms/HeaderUploadBtn";
import * as S from "./style";

export interface Props {
  src: string;
  text: string;
  isMenuClicked: boolean;
  isUploadClicked: boolean;
  setIsMenuCliecked: (value: boolean) => void;
  setIsUploadClicked: (value: boolean) => void;
}

const Header: React.FC<Props> = ({
  src,
  text,
  isMenuClicked,
  isUploadClicked,
  setIsMenuCliecked,
  setIsUploadClicked,
}): JSX.Element => {
  return (
    <S.Header>
      <HeaderUploadBtn
        src={src}
        isUploadClicked={isUploadClicked}
        setIsUploadClicked={setIsUploadClicked}
      />
      <Label type="logo" text={text} />
      <HamburgerBtn
        isMenuClicked={isMenuClicked}
        setIsMenuClicked={setIsMenuCliecked}
      />
    </S.Header>
  );
};

export default Header;
