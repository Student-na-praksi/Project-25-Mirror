import "./LoginButton-style.css";
import loginIcon from "@/assets/login-icon.png";

export const LoginButton = (props: any) => {
    return (
        // It has two classNames networkInterfaces. Frame and the one passed.
        <div className={`frame ${props.className}`}>
            <img className="login-icon" alt="Login icon" src={loginIcon} />
        </div>
    );
};