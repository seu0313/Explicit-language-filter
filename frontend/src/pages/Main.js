import React, { Fragment, useEffect, useState } from 'react'
import axios from 'axios'
import { FileUploader } from '../components/FileUpload'
import { Loading } from '../components/Loading'
import { createStyles } from '@material-ui/core';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const Main = () => {
    const [loading, setLoading] = useState(true)
    const [deeps, setDeeps] = useState([])

    useEffect(() => {
        const getData = async () => {
            await axios.get("http://127.0.0.1:8000/deeps/")
                .then((res) => {
                    setDeeps(res.data)
                    console.log(res.data)
                    setLoading(false)
                })
                .catch((error) => {
                    console.log('error')
                })
        }
        getData()
    }, [])

    if (loading){
        return <div style={styles.center}><Loading/></div>
    }
    return (
        <Fragment>
            <FileUploader />
            <hr/>
            <div style={styles.sectionStyle}>
                {deeps.map((deep) => (
                    <div key={deep.id}>{deep.video_file}</div>
                ))}
            </div>
        </Fragment>
    );
}

const styles = createStyles({
    center: {
        position: 'absolute', left: '50%', top: '50%',
        transform: 'translate(-50%, -50%)'
    },
    sectionStyle: {
        width: "100%",
        height: "800px",
        // background: "linear-gradient(#11998e, #38ef7d)",
    }
});

export default Main
