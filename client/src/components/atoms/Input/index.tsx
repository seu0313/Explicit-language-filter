import React from "react";
import * as S from "./style";

export interface Props {
  type?: string;
  accept?: string;
  width?: string;
  height?: string;
  fontSize?: string;
  placeholder?: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const Input: React.FC<Props> = ({
  type = "text",
  accept,
  width = "311px",
  height = "43px",
  fontSize = "13px",
  placeholder,
  onChange,
}): JSX.Element => {
  return (
    <S.Input
      type={type}
      accept={accept}
      width={width}
      height={height}
      fontSize={fontSize}
      placeholder={placeholder}
      onChange={onChange}
    />
  );
};

export default Input;
