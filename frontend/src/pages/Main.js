import React, { Component } from 'react'
import axios from 'axios'
import { FileUploader } from '../components/FileUpload'
import { Loading } from '../components/Loading'
import { createStyles } from '@material-ui/core';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

class Main extends Component {
    state = {
        loading : true,
        deeps : []
    }

    setLoading = (data) => {
        this.setState(data)
    }

    setDeeps = (data) => {
        this.setState(data)
    }

    componentDidMount = async () => {
        await axios.get("http://127.0.0.1:8000/deeps/")
                .then((res) => {
                    this.setDeeps({deeps: res.data})
                    console.log(res.data)
                    this.setLoading({loading: false})
                })
                .catch((error) => {
                    console.log(error)
                })
    }

    _renderData = () => {
        axios
            .get("http://127.0.0.1:8000/deeps/")
            .then((res) => {
                this.setDeeps({deeps: res.data})
            })
            .catch((error) => {
                console.log(error)
            })
    }

    render() {
        const {loading, deeps} = this.state

        if (loading){
            return <div style={styles.center}><Loading/></div>
        }

        return (
            <div>
                <FileUploader _renderData={this._renderData}/>
                <hr/>
                <div style={styles.sectionStyle}>
                    {deeps.map((deep) => (
                        <div key={deep.id}>{deep.video_file}</div>
                    ))}
                </div>
            </div>
        )
    }
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
