import React from "react";
import * as S from "./style";

export interface Props extends S.Props {
  isMenuClicked: boolean;
  setIsMenuClicked: (value: boolean) => void;
}

const HamburgerBtn: React.FC<Props> = ({
  isMenuClicked,
  setIsMenuClicked,
}): JSX.Element => {
  const onClick = (): void => {
    setIsMenuClicked(!isMenuClicked);
  };
  return (
    <S.HamburgerWrapper onClick={onClick} isMenuClicked={isMenuClicked}>
      <S.HamburgerList />
      <S.HamburgerList />
      <S.HamburgerList />
    </S.HamburgerWrapper>
  );
};

export default HamburgerBtn;
