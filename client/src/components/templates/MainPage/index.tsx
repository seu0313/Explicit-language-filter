import React, { useState, useEffect } from "react";
import Header from "components/modules/Header";
import cloud from "assets/image/cloud.png";
import thumbnail from "assets/image/thumbnail.png";
import thumbnail2 from "assets/image/thumbnail2.png";
import MainVideo from "components/modules/MainVideo";
import ModalContainer from "components/modules/ModalContainer";
import * as S from "./style";

const MainPage = (): JSX.Element => {
  const dummy = [
    {
      id: "1",
      text: "Mountains | Beautiful Chill Mix WAAAAA~",
      date: "2021-06-04T14:05:46.384Z",
      src: thumbnail2,
    },
    {
      id: "2",
      text: "Ocean | Beautiful Pacific WAAAAA~",
      date: "2021-05-23T14:05:46.384Z",
      src: thumbnail,
    },
    {
      id: "3",
      text: "Ocean | Beautiful Pacific WAAAAA~",
      date: "2021-05-23T14:05:46.384Z",
      src: thumbnail2,
    },
    {
      id: "4",
      text: "Ocean | Beautiful Pacific WAAAAA~",
      date: "2021-05-23T14:05:46.384Z",
      src: thumbnail,
    },
  ];

  const [isUploadClicked, setIsUploadClicked] = useState(false);
  const [isMenuClicked, setIsMenuClicked] = useState(false);
  const [isNotification, setIsNotification] = useState(false);

  useEffect(() => {
    // setTimeout(() => {
    //   setIsNotification(true);
    // }, 3000);
  }, []);

  return (
    <S.Container>
      <S.Elements>
        <Header
          src={cloud}
          text="LINGO FILTER"
          isMenuClicked={isMenuClicked}
          setIsMenuCliecked={setIsMenuClicked}
          isUploadClicked={isUploadClicked}
          setIsUploadClicked={setIsUploadClicked}
        />
        <div style={{ display: "inline-block", width: "343px" }} />
        {dummy.map((deep) => (
          <div>
            <MainVideo
              key={deep.id}
              id={deep.id}
              text={deep.text}
              date={deep.date}
              src={deep.src}
            />
            <div style={{ display: "inline-block", width: "343px" }} />
          </div>
        ))}
      </S.Elements>
      <ModalContainer
        isUploadClicked={isUploadClicked}
        setIsUploadClicked={setIsUploadClicked}
        isMenuClicked={isMenuClicked}
        setIsMenuClicked={setIsMenuClicked}
        isNotification={isNotification}
        setIsNotification={setIsNotification}
      />
    </S.Container>
  );
};

export default MainPage;
