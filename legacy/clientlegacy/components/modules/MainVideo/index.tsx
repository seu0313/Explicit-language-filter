import React from "react";
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
  return (
    <S.MainVideo>
      <VideoThumbnail src={src} />
      <S.MetaSection>
        <Label text={title} width="18.75rem" />
        <VideoCreatedAt createdAt={createdAt} />
      </S.MetaSection>
    </S.MainVideo>
  );
};

export default MainVideo;
