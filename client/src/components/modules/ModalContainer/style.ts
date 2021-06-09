import Modal from "styled-react-modal";
import theme from "styles/theme";

export interface Props {
  opacity: number;
}

export const ModalContainer = Modal.styled`
  width: ${theme.size.customWidth};
  background-color: white;
  opacity: ${(props: Props) => props.opacity};
  transition: all 0.3s ease-in-out;
`;
