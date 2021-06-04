import React, { useState } from "react";
import * as S from "./style";

export interface ModalContainerProps {
  isUploadClicked: boolean;
  setIsUploadClicked: (value: boolean) => void;
  isMenuClicked: boolean;
  setIsMenuClicked: (value: boolean) => void;
}

const ModalContainer: React.FC<ModalContainerProps> = ({
  isUploadClicked,
  setIsUploadClicked,
  isMenuClicked,
  setIsMenuClicked,
}): JSX.Element => {
  const [opacity, setOpacity] = useState(0);
  const toggleModal = () => {
    setOpacity(0);
    if (isUploadClicked) {
      setIsUploadClicked(!isUploadClicked);
    } else if (isMenuClicked) {
      setIsMenuClicked(!isMenuClicked);
    }
  };

  const afterOpen = () => {
    setTimeout(() => {
      setOpacity(1);
    }, 100);
  };

  const beforeClose = () => {
    return new Promise((resolve) => {
      setOpacity(0);
      setTimeout(resolve, 300);
    });
  };

  return (
    <S.Container>
      <S.ModalContainer
        // opacity={opacity}
        isOpen={isUploadClicked || isMenuClicked}
        afterOpen={afterOpen}
        beforeClose={beforeClose}
        onBackgroundClick={toggleModal}
        onEscapeKeydown={toggleModal}
        backgroundProps={{ opacity }}
      >
        {isMenuClicked === true ? (
          <div>
            임시
            <p>isMenuClicked: {String(isMenuClicked)}</p>
            <button type="button" onClick={toggleModal}>
              CLOSE
            </button>
          </div>
        ) : null}
        {isUploadClicked === true ? (
          <div>
            임시
            <p>isUploadClicked: {String(isUploadClicked)}</p>
            <button type="button" onClick={toggleModal}>
              CLOSE
            </button>
          </div>
        ) : null}
      </S.ModalContainer>
    </S.Container>
  );
};

export default ModalContainer;
