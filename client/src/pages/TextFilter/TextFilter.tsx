import React from "react";
import styled from "styled-components";
import TextForm from "../../components/TextForm";
import TextResult from "../../components/TextResult";

export default function TextFilter(): JSX.Element {
  return (
    <TextFilterContainer>
      <TextForm />
      <TextResult>dd</TextResult>
    </TextFilterContainer>
  );
}

const TextFilterContainer = styled.div`
  display: flex;
  height: 100%;
`;
