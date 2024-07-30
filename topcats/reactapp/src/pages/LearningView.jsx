import { useCallback, useState } from 'react';
import { pdfjs, Document, Page } from 'react-pdf';




pdfjs.GlobalWorkerOptions.workerSrc = new URL(
    'pdfjs-dist/build/pdf.worker.min.mjs',
    import.meta.url,
).toString();





export default function LearningView() {
    const [file, setFile] = useState('./sample.pdf');


    return (
        <div >
            <header>
                <h1>react-pdf sample page</h1>
            </header>
            <div class="embed-responsive" style={{ height: "100vh" }}>
                <embed
                    src="https://beej.us/guide/bgnet/pdf/bgnet_usl_c_1.pdf"
                    type="application/pdf"
                    width="100%"
                    height="100%"
                />
            </div>
        </div>
    );
}