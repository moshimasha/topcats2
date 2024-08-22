
import { pdfjs, Document, Page } from 'react-pdf';

import React, { useEffect, useState } from 'react';
import axios from 'axios';

import { useParams, useLocation } from 'react-router-dom';



export default function LearningView() {
    const [fileUrl, setFileUrl] = useState(null);

    const [isRecallActive, setIsRecallActive] = useState(false);

    const [questions, setQuestions] = useState([]);

    const { fileName } = useParams();

    useEffect(() => {
        // Fetch the PDF file from the backend
        //makeRequest();
        axios({
            url: 'http://localhost:8000/api/learn/' + fileName + '/', // Endpoint for the PDF file
            method: 'GET',
            responseType: 'blob', // Important for binary data like PDF
        })
            .then((response) => {
                // Create a URL for the PDF blob
                const fileBlob = new Blob([response.data], { type: 'application/pdf' });
                const url = window.URL.createObjectURL(fileBlob);
                setFileUrl(url);
                console.log(url);
            })
            .catch((error) => {
                console.error("Error fetching the PDF:", error);
            });
    }, []);

    //get page numberf and send
    const genQuestions = async () => {

        const response = await axios.get('http://localhost:8000/api/questions/', {
            params: {
                file_name: fileName,
                page_no: 0,
                num_questions: 5
            }
        }).then(response => {
            console.log(response.data);
        }).catch(error => {
            console.error(error);
        });

    };

    if(!isRecallActive){
    return (
        
        <div >
            <header>
                <h1>react-pdf sample page</h1>
            </header>

            <button className="form-button" type="submit" onClick ={genQuestions} >
                generate questions
            </button>

            <iframe
                src={fileUrl}
                title={"titel"}
                width="100%"
                height="600px"
                style={{ border: 'none' }}
            />
        </div>
    
    );
    } else {
        return(
            <div >
            <header>
                <h1>react-pdf sample page</h1>
            </header>

            <p> question </p>

            <input
                className="form-input"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
            />

            <iframe
                src={fileUrl}
                title={"titel"}
                width="100%"
                height="600px"
                style={{ border: 'none' }}
            />
        </div>


        );
    }
}