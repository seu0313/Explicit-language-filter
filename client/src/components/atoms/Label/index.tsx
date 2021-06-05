import React from "react";
import * as S from "./style";

export interface Props {
  type?: string;
  fontSize?: string;
  width?: string;
  text: string;
}

const Label: React.FC<Props> = ({
  type,
  fontSize = "18px",
  text,
  width = "9rem",
}): JSX.Element => {
  if (type === "text") {
    return (
      <S.Label width={width}>
        <S.LabelText fontSize={fontSize}>{text}</S.LabelText>
      </S.Label>
    );
  }

  const logotitle = text.split(" ");

  return (
    <S.Label width={width}>
      <S.LabelText fontSize={fontSize}>{logotitle[0]}</S.LabelText>
      <S.LabelLogo fontSize={fontSize}>{logotitle[1]}</S.LabelLogo>
    </S.Label>
  );
};

export default Label;
