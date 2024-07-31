import axios from "axios";
import React, { useState, useEffect } from 'react';

import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';


export default function LibraryView() {
    const [files, setFiles] = useState([]);
    useEffect(() => {
        makeRequest();
    }, [])

    const makeRequest = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/library/'); // Replace with your API endpoint
            const data = response.data;

            // Check for errors in the response

            // Extract names from the data
            const extractedNames = data.map(item => item.name);
            setFiles(extractedNames);
        } catch (err) {
        } finally {
        }
    };

    return (
        <div >
            <h2>Files List</h2>
            <ul>
                {files.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );

}

/*
file names should be links that lead to instance of pdf view page for that specific file

learningView makes api request to load specific file from the database

<ul>
                {files.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
*/