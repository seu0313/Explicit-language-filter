import React from "react";
import * as S from "./style";

export interface HeaderTextProps {
  text: string;
}

const HeaderText: React.FC<HeaderTextProps> = ({ text }): JSX.Element => {
  const textList = text.split(" ");

  return (
    <S.Container>
      <S.HeaderTextLeft>{textList[0]}</S.HeaderTextLeft>
      <S.HeaderTextRight>{textList[1]}</S.HeaderTextRight>
    </S.Container>
  );
};

export default HeaderText;
