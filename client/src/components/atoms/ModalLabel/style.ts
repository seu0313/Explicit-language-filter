import styled from "styled-components";

export interface Props {
  size: string;
}

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 165px;
`;
export const ModalLabel = styled.div<Props>`
  font-weight: bold;
  font-size: ${(props) => props.size};
  color: #000000;
`;
