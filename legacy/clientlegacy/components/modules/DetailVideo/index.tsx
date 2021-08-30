import React from "react";
import { Player } from "video-react";
import Label from "components/atoms/Label";
import Text from "components/atoms/Text";
import Button from "components/atoms/Button";
import VideoCreatedAt from "components/atoms/VideoCreatedAt";
import * as S from "./style";

export interface Props {
  id: string;
  title: string;
  description: string;
  createdAt: string;
  src: string;
  onClick: () => void;
}

const DetailVideo: React.FC<Props> = ({
  id,
  title,
  description,
  createdAt,
  src,
  onClick,
}): JSX.Element => {
  return (
    <S.DetailVideo>
      <Player key={id} width="343px" height="200px" src={src} />
      <S.MetaSection>
        <br/>
        <Label text={title} width="18.75rem" />
        <br/>
        <Text text={description} />
        <br/>
        <VideoCreatedAt createdAt={createdAt} />
        <br/>
      </S.MetaSection>
        <Button type="button" value="삭제" onClick={onClick}/>
    </S.DetailVideo>
  );
};

export default DetailVideo;
