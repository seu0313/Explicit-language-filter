import React, { useState } from "react";
import { useSetRecoilState } from "recoil";
import styled from "styled-components";
import { testAtomState } from "../../atoms/testAtom";
import theme from "../../styles/theme";

export default function TextArea(): JSX.Element {
  const [text, setText] = useState("");
  const setState = useSetRecoilState(testAtomState);
  const placeholder = "비속어가 포함된 단어를 입력해주십시오.";

  const onChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    e.preventDefault();
    setText(e.target.value);
    const val = text.replace(/[^가-힣]/, "*");
    setState(val);
  };

  const onSubmit = (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
  };

  return (
    <TextAreaContainer>
      <TextAreaElement
        value={text}
        autoFocus
        maxLength={500}
        placeholder={placeholder}
        onChange={onChange}
      />
      <button
        type="submit"
        style={{
          width: "67vh",
          height: "40px",
          backgroundColor: "yellowgreen",
          borderRadius: "5px",
          // border: "1px yellowgreen solid",
        }}
        onSubmit={onSubmit}
      >
        변환하기
      </button>
    </TextAreaContainer>
  );
}

const TextAreaElement = styled.textarea`
  width: 100%;
  height: 100%;
  padding: 1rem;
  resize: none;
  border: 1px solid ${theme.color.basicColor};
  border-radius: 0.5rem;
  font-size: 1rem;
  font-family: Arial, Helvetica, sans-serif;

  &:active {
    border-color: ${theme.color.primaryAccentTextLight};
  }
`;

const TextAreaContainer = styled.form`
  width: 60vh;
  height: 70vh;
`;
