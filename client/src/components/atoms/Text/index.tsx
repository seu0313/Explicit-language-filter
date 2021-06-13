import React from "react";
import * as S from "./style";

export interface Props {
  type?: string;
  fontSize?: string;
  width?: string;
  text: string;
}

const Text: React.FC<Props> = ({ fontSize = "16px", text }): JSX.Element => {
  return (
    <S.TextWrapped>
      <S.Text fontSize={fontSize}>{text}</S.Text>
    </S.TextWrapped>
  );
};

export default Text;
