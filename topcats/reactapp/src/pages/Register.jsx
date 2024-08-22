import Form from "../components/Form"

const Register = () => {
    return (
        <div>
            <TopBar />
            <Form route="/api/login/" method="register" />
        </div>
    );
}

export default Register