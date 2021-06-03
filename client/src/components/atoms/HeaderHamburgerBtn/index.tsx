import React from "react";
import * as S from "./style";

export interface HeaderHamburgerBtnProps extends S.Props {
  isMenuClicked: boolean;
  setIsMenuClicked: (value: boolean) => void;
}

const HeaderHamburgerBtn: React.FC<HeaderHamburgerBtnProps> = ({
  isMenuClicked,
  setIsMenuClicked,
}) => {
  const onClickMenuBtn = (): void => {
    setIsMenuClicked(!isMenuClicked);
  };
  return (
    <S.Container>
      <S.HeaderHamburgerWrapper
        onClick={onClickMenuBtn}
        isMenuClicked={isMenuClicked}
      >
        <S.HeaderHamburgerList />
        <S.HeaderHamburgerList />
        <S.HeaderHamburgerList />
      </S.HeaderHamburgerWrapper>
    </S.Container>
  );
};

export default HeaderHamburgerBtn;
