import React from "react";
import Label from "components/atoms/Label";
import HamburgerBtn from "components/atoms/HamburgerBtn";
import HeaderUploadBtn from "components/atoms/HeaderUploadBtn";
import cloud from "assets/image/cloud.png";
import * as S from "./style";

export interface Props {
  isMenuClicked: boolean;
  isUploadClicked: boolean;
  setIsMenuCliecked: (value: boolean) => void;
  setIsUploadClicked: (value: boolean) => void;
}

const Header: React.FC<Props> = ({
  isMenuClicked,
  isUploadClicked,
  setIsMenuCliecked,
  setIsUploadClicked,
}): JSX.Element => {
  return (
    <S.Header>
      <HeaderUploadBtn
        src={cloud}
        isUploadClicked={isUploadClicked}
        setIsUploadClicked={setIsUploadClicked}
      />
      <Label type="logo" text="LINGO FILTER" />
      <HamburgerBtn
        isMenuClicked={isMenuClicked}
        setIsMenuClicked={setIsMenuCliecked}
      />
    </S.Header>
  );
};

export default Header;
