import React from "react";
import { useHistory } from "react-router-dom";
import VideoTitle from "components/atoms/VideoTitle";
import VideoCreatedAt from "components/atoms/VideoCreatedAt";
import VideoThumbnail from "components/atoms/VideoThumbnail";
import * as S from "./style";

export interface MainVideoProps {
  id: string;
  text: string;
  date: string;
  src: string;
}

const MainVideo: React.FC<MainVideoProps> = ({
  id,
  text,
  date,
  src,
}): JSX.Element => {
  const history = useHistory();

  const onClickMainVideo = () => {
    const path = `/detail/${id}`;
    history.push(path);
  };

  return (
    <S.Container onClick={onClickMainVideo}>
      <VideoThumbnail src={src} />
      <S.MetaSection>
        <S.MetaSectionTop>
          <VideoTitle text={text} />
        </S.MetaSectionTop>
        <S.MetaSectionBottom>
          <VideoCreatedAt date={date} />
        </S.MetaSectionBottom>
      </S.MetaSection>
    </S.Container>
  );
};

export default MainVideo;
