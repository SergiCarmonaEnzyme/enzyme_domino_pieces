from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import pysftp as sftp
import pandas as pd
from io import StringIO

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

    def readFileContent(self, remote_path, filename):
        try:

            path_file = remote_path + "/" + filename

            print(
                f"read file from {self.hostname} as {self.username} [(remote path : {path_file});]"
            )

            sftp_doc = self.connection.open(path_file)

            contentDoc = sftp_doc.read()

            df_file = pd.read_csv(StringIO(contentDoc.decode("utf-8-sig", errors='ignore')), sep=";")

            print("read file completed")

            return df_file.astype(str)

        except Exception as err:
            raise Exception(err)

class ReadFileSFTPPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info("Start Read File in SFTP.")
        
        sftp = Sftp(
            hostname=input_data.host,
            username=input_data.user,
            password=input_data.password,
            port=input_data.port
        )
        sftp.connect()
        
        csv_doc = sftp.readFileContent(remote_path=input_data.route, filename=input_data.file)
        csv_doc = csv_doc.astype(str)

        self.logger.info(f" INFO DOC = {csv_doc}")
        
        sftp.disconnect()

        # Return success message
        return OutputModel(message="OK")
