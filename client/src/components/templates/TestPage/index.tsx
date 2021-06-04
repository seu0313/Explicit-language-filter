import React, { useState } from "react";

// Test page
import ModalLabel from "components/atoms/ModalLabel";
import UploadModalTitleInput from "components/atoms/UploadModalTitleInput";
import UploadModalDescInput from "components/atoms/UploadModalDescInput";
import UploadModalFileInput from "components/atoms/UploadModalFileInput";
import UploadModalBtn from "components/atoms/UploadModalBtn";
import * as S from "./style";

const TestPage = (): JSX.Element => {
  return (
    <div>
      <ModalLabel text="비속어 필터링하기" />
    </div>
  );
};

export default TestPage;
