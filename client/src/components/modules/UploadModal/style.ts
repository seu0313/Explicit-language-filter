import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const UploadModal = styled.form`
  display: inline-block;
  width: 343px;
  height: 400px;
  justify-content: center;
  align-items: center;
`;

export const UploadModalHeader = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 50px;
`;

export const UploadModalContent = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  // align-items: flex-start;
`;

export const UploadModalContentElement = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
`;

export const UploadModalFooter = styled.div`
  display: block;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  padding-left: 16px;
`;
