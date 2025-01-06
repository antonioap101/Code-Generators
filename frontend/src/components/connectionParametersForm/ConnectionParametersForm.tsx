import React from "react";
import { ConnectionParameters } from "../../constants/CRUDCodeGeneratorInput.ts";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDatabase, faPlug, faServer } from "@fortawesome/free-solid-svg-icons";
import styles from "./ConnectionParametersForm.module.css";

interface ConnectionParametersFormProps {
    parameters?: ConnectionParameters;
    setParameters: (params: ConnectionParameters) => void;
}

const ConnectionParametersForm: React.FC<ConnectionParametersFormProps> = ({ parameters, setParameters }) => {
    const handleChange = (key: keyof ConnectionParameters, value: string | number) => {
        setParameters({
            ...parameters,
            [key]: value,
        } as ConnectionParameters);
    };

    return (
        <div className={styles.container}>
            {/* Host Field */}
            <div className={styles.field}>
                <FontAwesomeIcon icon={faServer} />
                <input
                    type="text"
                    placeholder="Host"
                    value={parameters?.host || ""}
                    onChange={(e) => handleChange("host", e.target.value)}
                    className={styles.input}
                />
            </div>

            {/* Port Field */}
            <div className={styles.field}>
                <FontAwesomeIcon icon={faPlug} />
                <input
                    type="number"
                    placeholder="Port"
                    value={parameters?.port || ""}
                    onChange={(e) => handleChange("port", parseInt(e.target.value, 10))}
                    className={styles.input}
                />
            </div>

            {/* Database Name Field */}
            <div className={styles.field}>
                <FontAwesomeIcon icon={faDatabase} />
                <input
                    type="text"
                    placeholder="Database Name"
                    value={parameters?.database_name || ""}
                    onChange={(e) => handleChange("database_name", e.target.value)}
                    className={styles.input}
                />
            </div>
        </div>
    );
};

export default ConnectionParametersForm;