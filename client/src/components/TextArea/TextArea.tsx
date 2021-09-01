import React from "react";
import styled from "styled-components";
import theme from "../../styles/theme";

type TextAreaProps = React.TextareaHTMLAttributes<HTMLTextAreaElement>;

export default function TextArea(props: TextAreaProps): JSX.Element {
  return (
    <TextAreaContainer>
      <textarea {...props} />
    </TextAreaContainer>
  );
}

const TextAreaContainer = styled.div`
  width: 85%;
  height: 70vh;

  textarea {
    width: inherit;
    height: inherit;
    padding: 1rem;
    resize: none;
    border: 1px solid ${theme.color.basicColor};
    border-radius: 0.5rem;
    font-size: 0.9rem;
    font-family: Arial, Helvetica, sans-serif;

    &:active {
      border-color: ${theme.color.primaryAccentTextLight};
    }
  }
`;
