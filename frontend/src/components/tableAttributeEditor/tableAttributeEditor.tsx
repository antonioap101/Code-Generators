import React from "react";
import "./tableAttributeEditor.css";
import {TypeEnum} from "../../constants/TypeEnum";
import {FieldModel} from "../../constants/CRUDCodeGeneratorInput.ts";
import TableRow from "./rows/TableRow.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faPlus} from "@fortawesome/free-solid-svg-icons";

interface TableAttributeEditorProps {
    fields: FieldModel[];
    setFields: (fields: FieldModel[]) => void;
}

const TableAttributeEditor: React.FC<TableAttributeEditorProps> = ({ fields, setFields }) => {
    const handleFieldChange = <K extends keyof FieldModel>(
        index: number,
        key: K,
        value: FieldModel[K]
    ) => {
        const updatedFields = [...fields];
        updatedFields[index][key] = value;

        // Ensure only one primary key
        if (key === "primaryKey" && value) {
            updatedFields.forEach((field, i) => {
                if (i !== index) field.primaryKey = false;
            });
        }

        setFields(updatedFields);
    };

    const addField = () => {
        setFields([...fields, { name: "", type: TypeEnum.TEXT, nullable: true, unique: false }]);
    };

    const removeField = (index: number) => {
        const updatedFields = fields.filter((_, i) => i !== index);

        // Ensure at least one primary key
        if (!updatedFields.some((field) => field.primaryKey)) {
            updatedFields[0].primaryKey = true;
        }

        setFields(updatedFields);
    };

    return (
        <div className="table-attribute-editor">
            <div className="table-header">
                <div className="table-cell">Nombre</div>
                <div className="table-cell">Tipo</div>
                <div className="table-cell">Nullable</div>
                <div className="table-cell">Unique</div>
                <div className="table-cell">AutoIncrement</div>
                <div className="table-cell">Primary Key</div>
                <div className="table-cell">
                    <button className="field-button" onClick={addField}>
                        <FontAwesomeIcon icon={faPlus} />
                    </button>
                </div>
            </div>
            {fields.map((field, index) => (
                <TableRow
                    key={index}
                    field={field}
                    index={index}
                    isPrimaryKeyDisabled={field.primaryKey}
                    onFieldChange={handleFieldChange}
                    onRemove={index > 0 ? () => removeField(index) : undefined}
                />
            ))}
        </div>
    );
};

export default TableAttributeEditor;