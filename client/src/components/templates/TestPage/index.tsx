import React, { useState } from "react";

// Test page
import TEST from "components/atoms/Label";
// import * as S from "./style";

const TestPage = (): JSX.Element => {
  const [isMenuClicked, setIsMenuClicked] = useState(false);

  return (
    <div>
      <TEST type="text" fontSize="18px" width="18.75rem" text="LINGO FILTER" />
    </div>
  );
};

export default TestPage;
