import React from "react";
import { useHistory } from "react-router-dom";
import Label from "components/atoms/Label";
import VideoCreatedAt from "components/atoms/VideoCreatedAt";
import VideoThumbnail from "components/atoms/VideoThumbnail";
import * as S from "./style";

export interface Props {
  id: string;
  title: string;
  createdAt: string;
  src: string;
}

const MainVideo: React.FC<Props> = ({
  id,
  title,
  createdAt,
  src,
}): JSX.Element => {
  const history = useHistory();

  const onClick = () => {
    const path = `/detail/${id}`;
    history.push(path);
  };

  return (
    <S.MainVideo onClick={onClick}>
      <VideoThumbnail src={src} />
      <S.MetaSection>
        <Label text={title} width="18.75rem" />
        <VideoCreatedAt createdAt={createdAt} />
      </S.MetaSection>
    </S.MainVideo>
  );
};

export default MainVideo;
