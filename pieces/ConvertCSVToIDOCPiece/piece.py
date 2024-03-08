from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import pandas as pd
from io import StringIO
import xml.etree.ElementTree as ET


def _convertDFToIDoc(file_content):

    df_doc = pd.read_csv(StringIO(file_content), sep=";")

    idoc = ET.Element("DEUTORS")
    current_order_id = None
    order_element = None

    for index, row in df_doc.iterrows():
        if row['persona'] != current_order_id:
            if order_element is not None:
                idoc.append(order_element)

            order_element = ET.SubElement(idoc, "DEUTOR", PERSONA=str(row['persona']), CONTRATO=str(row['contrato']))
            deutor_info_element = ET.SubElement(order_element, "INFO")
            ET.SubElement(deutor_info_element, "nombre").text = str(row['nombre'])
            ET.SubElement(deutor_info_element, "apellido_1").text = str(row['apellido_1'])
            ET.SubElement(deutor_info_element, "apellido_2").text = str(row['apellido_2'])
            ET.SubElement(deutor_info_element, "nif").text = str(row['nif'])
            ET.SubElement(deutor_info_element, "telefono_1").text = str(row['telefono_1'])
            ET.SubElement(deutor_info_element, "telefono_3").text = str(row['telefono_3'])
            ET.SubElement(deutor_info_element, "situacion").text = str(row['situacion'])

            current_order_id = row['persona']

        if order_element is not None:
            idoc.append(order_element)

    idoc_doc = ET.tostring(idoc, encoding='utf-8').decode('utf-8')

    print(f"IDOC = {idoc_doc}")
    
    return str(idoc_doc)

class ConvertCSVToIDOCPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info("Start convert file content into IDOC.")

        idoc_content_string = _convertDFToIDoc(input_data.file_content)

        self.logger.info("Finish convert file content into IDOC.")
        
        # Return success message
        return OutputModel(idoc_content=idoc_content_string)
