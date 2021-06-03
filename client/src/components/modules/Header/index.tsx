import React from "react";
import HeaderHamburgerBtn from "components/atoms/HeaderHamburgerBtn";
import HeaderText from "components/atoms/HeaderText";
import HeaderUploadBtn from "components/atoms/HeaderUploadBtn";
import * as S from "./style";

export interface HeaderProps {
  src: string;
  text: string;
  isMenuClicked: boolean;
  setIsMenuCliecked: (value: boolean) => void;
  isUploadClicked: boolean;
  setUploadClicked: (value: boolean) => void;
}

const Header: React.FC<HeaderProps> = ({
  src,
  text,
  isMenuClicked,
  setIsMenuCliecked,
  isUploadClicked,
  setUploadClicked,
}) => {
  return (
    <S.Container>
      <S.HeaderLeft>
        <HeaderUploadBtn
          src={src}
          isUploadClicked={isUploadClicked}
          setUploadClicked={setUploadClicked}
        />
      </S.HeaderLeft>
      <S.HeaderCenter>
        <HeaderText text={text} />
      </S.HeaderCenter>
      <S.HeaderRight>
        <HeaderHamburgerBtn
          isMenuClicked={isMenuClicked}
          setIsMenuClicked={setIsMenuCliecked}
        />
      </S.HeaderRight>
    </S.Container>
  );
};

export default Header;
