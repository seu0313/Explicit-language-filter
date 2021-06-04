import styled from "styled-components";
import { BaseModalBackground } from "styled-react-modal";

const FadingBackground = styled(BaseModalBackground)`
  opacity: ${(props: any) => props.opacity};
  transition: all 0.3s ease-in-out;
`;

export default FadingBackground;
