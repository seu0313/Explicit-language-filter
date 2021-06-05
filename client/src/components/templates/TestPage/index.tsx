import React, { useState } from "react";

// Test page
import TEST from "components/atoms/HamburgerBtn";
// import * as S from "./style";

const TestPage = (): JSX.Element => {
  const [isMenuClicked, setIsMenuClicked] = useState(false);

  return (
    <div>
      <TEST isMenuClicked={isMenuClicked} setIsMenuClicked={setIsMenuClicked} />
    </div>
  );
};

export default TestPage;
