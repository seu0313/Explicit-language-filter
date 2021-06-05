import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "components/modules/Header";
import cloud from "assets/image/cloud.png";
import thumbnail from "assets/image/thumbnail.png";
import thumbnail2 from "assets/image/thumbnail2.png";
import MainVideo from "components/modules/MainVideo";
import ModalContainer from "components/modules/ModalContainer";
import * as S from "./style";

const MainPage = (): JSX.Element => {
  const [deeps, setDeeps] = useState<any[]>([]);

  useEffect(() => {
    const url = "http://127.0.0.1:8000/api/v1/deeps/";
    axios
      .get(url)
      .then((res) => {
        setDeeps(res.data.data);
        // console.log(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  const dummy = [
    {
      id: "1",
      title: "Mountains | Beautiful Chill Mix WAAAAA~",
      createdAt: "2021-06-04T14:05:46.384Z",
      src: thumbnail2,
    },
    {
      id: "2",
      title: "Ocean | Beautiful Pacific WAAAAA~",
      createdAt: "2021-05-23T14:05:46.384Z",
      src: thumbnail,
    },
    {
      id: "3",
      title: "Ocean | Beautiful Pacific WAAAAA~",
      createdAt: "2021-05-23T14:05:46.384Z",
      src: thumbnail2,
    },
    {
      id: "4",
      title: "Ocean | Beautiful Pacific WAAAAA~",
      createdAt: "2021-05-23T14:05:46.384Z",
      src: thumbnail,
    },
  ];

  const [isUploadClicked, setIsUploadClicked] = useState(false);
  const [isMenuClicked, setIsMenuClicked] = useState(false);
  const [isNotification, setIsNotification] = useState(false);

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
              text={deep.title}
              date={deep.createdAt}
              src={thumbnail2}
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
