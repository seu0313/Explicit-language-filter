import styled from "styled-components";
import theme from "styles/theme";

export interface Props {
  width: string;
}

export const VideoThumbnail = styled.img<Props>`
  width: ${theme.size.customWidth};
`;
