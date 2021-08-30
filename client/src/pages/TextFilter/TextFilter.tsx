import React from "react";
import { useRecoilValue } from "recoil";
import styled from "styled-components";
import { testAtomState } from "../../atoms/testAtom";
import TextArea from "../../components/TextArea";

export default function TextFilter(): JSX.Element {
  const state = useRecoilValue(testAtomState);
  return (
    <TextFilterContainer>
      <TextArea />
      <div className="text-filter-result">{state}</div>
    </TextFilterContainer>
  );
}

const TextFilterContainer = styled.div`
  display: flex;
  justify-content: left;
  align-items: center;

  .text-filter-result {
    width: 50vh;
    margin-left: 5rem;
    font-size: 1rem;
  }
`;
