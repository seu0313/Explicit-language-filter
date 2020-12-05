import React, { useState, useEffect } from 'react';

// added
import axios from 'axios';

// design
import { createStyles, } from '@material-ui/core';
import './HomePage.scss';

// components
import { Loading } from '../components/Loading';
import { VideoGrid } from '../components/Video';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const HomePage = () => {
    // state
    const [LoadingCheck, setLoadingCheck] = useState(false);
    const [Deeps, setDeeps] = useState([]);

    // lifecycle
    useEffect(() => {
        let url = "http://127.0.0.1:8000/api/v1/deeps/";
        axios
            .get(url)
            .then((res) => {
                setDeeps(res.data);
                setLoadingCheck(true);
            })
            .catch((err) => console.log(err));
    },[]);

    // func
    const _renderData = () => {
        let url = "http://127.0.0.1:8000/api/v1/deeps/";
        axios
            .get(url)
            .then((res) => {
                setDeeps(res.data);
            })
            .catch((err) => console.log(err));
    }
    
    // render
    return(
        <div className='home'>
            <div className="responsive-video-grid-container">
                { !LoadingCheck ? 
                    <div style={styles.center}><Loading/></div> : 
                    <VideoGrid 
                        Deeps={Deeps} 
                        _renderData={_renderData} 
                        hideDivider={true}
                    />
                }
            </div>
        </div>
    );
}

const styles = createStyles({
    center: {
        position: 'absolute', left: '50%', top: '50%',
        transform: 'translate(-50%, -50%)'
    },
});

export default HomePage;