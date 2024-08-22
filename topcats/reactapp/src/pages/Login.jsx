import Form from "../components/Form"
import TopBar from "../components/TopBar";

const Login = () => {
    return (
        <div>
            <TopBar />
            <Form route="/api/login/" method="login" />
        </div>
    );
}

export default Login