import { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { useDynamicProperty } from "taipy-gui";

interface MarkdownProps {
    id?: string;
    classname?: string;
    defaultClassname?: string;
    content?: string;
    defaultContent: string;
}

const Markdown = (props: MarkdownProps) => {
    const { id } = props;
    const classname = useDynamicProperty(props.classname, props.defaultClassname, "");
    const contentDynamicProperty = useDynamicProperty(props.content, props.defaultContent, "")

    const [content, setContent] = useState("");

    useEffect(() => {
        setContent(contentDynamicProperty);
    }, [contentDynamicProperty]);

    return (
        <div id={id} className={classname}>
            <ReactMarkdown children={content} />
        </div>
    );
}

export default Markdown;
