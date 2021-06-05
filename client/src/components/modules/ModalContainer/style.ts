import styled from "styled-components";
import Modal from "styled-react-modal";

export interface Props {
  opacity: number;
}

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const ModalContainer = Modal.styled`
  width: 343px;
  background-color: white;
  opacity: ${(props: Props) => props.opacity};
  transition: all 0.3s ease-in-out;
`;
