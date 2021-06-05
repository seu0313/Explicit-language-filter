import styled from "styled-components";
import { BaseModalBackground } from "styled-react-modal";

export interface Props {
  opacity: number;
}

const FadingBackground = styled(BaseModalBackground)`
  opacity: ${(props: Props) => props.opacity};
  transition: all 0.3s ease-in-out;
`;

export default FadingBackground;
