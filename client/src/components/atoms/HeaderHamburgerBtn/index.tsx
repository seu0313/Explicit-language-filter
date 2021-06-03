import React from "react";
import * as S from "./style";

export interface HeaderHamburgerProps extends S.Props {
  isMenuClicked: boolean;
  setIsMenuClicked: (value: boolean) => void;
}

const HeaderHamburgerBtn: React.FC<HeaderHamburgerProps> = ({
  isMenuClicked,
  setIsMenuClicked,
}) => {
  const onClickMenu = (): void => {
    setIsMenuClicked(!isMenuClicked);
  };
  return (
    <S.HeaderHamburgerWrapper
      onClick={onClickMenu}
      isMenuClicked={isMenuClicked}
    >
      <S.HeaderHamburgerList />
      <S.HeaderHamburgerList />
      <S.HeaderHamburgerList />
    </S.HeaderHamburgerWrapper>
  );
};

export default HeaderHamburgerBtn;
