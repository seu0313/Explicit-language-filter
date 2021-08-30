import styled from "styled-components";
import theme from "styles/theme";

export const VideoCreatedAt = styled.div`
  font-size: 12px;
  width: 300px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: ${theme.color.tertiaryText};
`;
