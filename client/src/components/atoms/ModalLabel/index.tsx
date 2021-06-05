import React from "react";
import * as S from "./style";

export interface ModalLabelProps {
  size?: string;
  text: string;
}

const ModalLabel: React.FC<ModalLabelProps> = ({
  size = "18px",
  text,
}): JSX.Element => {
  return (
    <S.Container>
      <S.ModalLabel size={size}>{text}</S.ModalLabel>
    </S.Container>
  );
};

export default ModalLabel;
