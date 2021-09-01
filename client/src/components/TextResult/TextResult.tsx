import React from "react";
import styled from "styled-components";

type TextResultProps = {
  children?: React.ReactNode;
};

export default function TextResult({ children }: TextResultProps): JSX.Element {
  return <TextResultContainer>{children}</TextResultContainer>;
}

const TextResultContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;

  font-family: Arial, Helvetica, sans-serif;
  font-weight: 600;
  font-size: 1.5rem;
`;
