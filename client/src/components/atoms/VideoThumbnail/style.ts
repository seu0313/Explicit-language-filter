import styled from "styled-components";

export interface Props {
  width: string;
}

export const VideoThumbnail = styled.img<Props>`
  width: ${(props: Props) => props.width};
`;
