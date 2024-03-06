from domino.testing import piece_dry_run

def test_read_file_sftp_piece():
    input_data = dict(
        host="52.208.16.130",
        port="22",
        user="sftp_user",
        password="user",
        route="/sftp_user/files",
        file="Deutors_10.csv"
    )
    """output_data = piece_dry_run(
        "ReadFileSFTPPiece",
        input_data,
    )"""

    #assert output_data["message"] is not None