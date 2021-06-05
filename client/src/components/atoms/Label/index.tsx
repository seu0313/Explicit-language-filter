import React from "react";
import * as S from "./style";

export interface Props {
  type?: string;
  size?: string;
  width?: string;
  text: string;
}

const Label: React.FC<Props> = ({
  type,
  size = "18px",
  text,
  width = "9rem",
}): JSX.Element => {
  if (type === "text") {
    return (
      <S.Label width={width}>
        <S.LabelText size={size}>{text}</S.LabelText>
      </S.Label>
    );
  }

  const logotitle = text.split(" ");

  return (
    <S.Label width={width}>
      <S.LabelText size={size}>{logotitle[0]}</S.LabelText>
      <S.LabelLogo size={size}>{logotitle[1]}</S.LabelLogo>
    </S.Label>
  );
};

export default Label;
