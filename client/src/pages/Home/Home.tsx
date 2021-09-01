import React from "react";

const Home = (): JSX.Element => {
  return (
    <div>
      <h1>개발 일지</h1>
      <hr />
      <br />
      <ul>
        <li>
          <b>2021.08.30</b> | 사이드바, 메인 화면 레이아웃 구현
        </li>
        <li>
          <b>2021.08.31</b> | 텍스트 필터 UI/UX 구현
        </li>
        <li>
          <b>2021.09.02</b> | 텍스트 필터 컴포넌트 구현
        </li>
      </ul>
    </div>
  );
};

export default Home;
