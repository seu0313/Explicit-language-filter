import styled from "styled-components";
import theme from "styles/theme";

export const UploadModal = styled.form`
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  width: ${theme.size.customWidth};
  height: 400px;
`;
