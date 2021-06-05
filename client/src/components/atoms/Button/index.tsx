import React from "react";
import * as S from "./style";

export interface Props {
  type?: string;
  width?: string;
  height?: string;
  value?: string;
  fontSize?: string;
}

const Button: React.FC<Props> = ({
  type = "submit",
  width = "311px",
  height = "43px",
  value = "제출",
  fontSize = "16px",
}): JSX.Element => {
  return (
    <S.Button
      type={type}
      value={value}
      width={width}
      height={height}
      fontSize={fontSize}
    />
  );
};

export default Button;
