import React, { useState } from "react";
import styled from "styled-components";
import Button from "../../components/Button";
import TextArea from "../../components/TextArea";

export default function TextForm(): JSX.Element {
  const [originText, setOriginText] = useState("");

  const onChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setOriginText(e.target.value);
  };

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      console.log("API 전송");
    } catch (err) {
      console.log(err);
      setOriginText("");
    }
  };

  return (
    <TextFormContainer onSubmit={onSubmit}>
      {originText}
      <TextArea
        style={{ width: "90%", height: "85%" }}
        value={originText}
        onChange={onChange}
        placeholder="비속어가 포함된 단어를 입력해주십시오."
      />
      <Button type="submit" style={{ width: "82%" }}>
        변환하기
      </Button>
    </TextFormContainer>
  );
}

const TextFormContainer = styled.form`
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: left;
`;
