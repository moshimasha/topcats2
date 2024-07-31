import { useCallback, useState } from 'react';
import { pdfjs, Document, Page } from 'react-pdf';

export default function LearningView({file}) {

    return (
        <div >
            <header>
                <h1>react-pdf sample page</h1>
            </header>
            <div class="embed-responsive" style={{ height: "100vh" }}>
                <embed
                    src={file}
                    type="application/pdf"
                    width="100%"
                    height="100%"
                />
            </div>
        </div>
    );
}