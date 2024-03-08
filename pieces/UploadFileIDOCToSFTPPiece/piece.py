from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import pandas as pd
from io import StringIO
import xml.etree.ElementTree as ET

class Sftp:
    def __init__(self, hostname, username, password, port=22):
        """Constructor Method"""

        # Set connection object to None (initial value)
        self.cnopts = sftp.CnOpts()
        self.cnopts.hostkeys = None
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        try:
            # Get the sftp connection object
            self.connection = sftp.Connection(
                host=self.hostname,
                username=self.username,
                password=self.password,
                port=self.port,
                cnopts=self.cnopts
            )
        except Exception as err:
            raise Exception(err)
        finally:
            print(f"Connected to {self.hostname} as {self.username}.")

    def disconnect(self):
        self.connection.close()
        print(f"Disconnected from host {self.hostname}")

    def saveFileContent(self, remote_path, filename, data):
        try:
            path_file = remote_path + "/" + filename

            file = StringIO(data)
            file.seek(0)
            self.connection.putfo(file, path_file)

            print("upload file completed")

        except Exception as err:
            raise Exception(err)


class UploadFileIDOCToSFTPPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info("Start Read File in SFTP.")
        
        sftp = Sftp(
            hostname=input_data.host,
            username=input_data.user,
            password=input_data.password,
            port=input_data.port
        )
        sftp.connect()
        
        sftp.saveFileContent(remote_path=input_data.route, filename=input_data.file, data=input_data.idoc_content)
        
        sftp.disconnect()
