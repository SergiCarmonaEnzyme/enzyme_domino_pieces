FROM ghcr.io/tauffer-consulting/domino-base-piece:latest

# Install specific requirements
RUN apt update
RUN apt install ffmpeg -y

# Need to copy pieces source code
COPY config.toml domino/pieces_repository/
COPY pieces domino/pieces_repository/pieces
COPY .domino domino/pieces_repository/.domino

# Install specific python dependencies
RUN pip install --no-cache-dir numpy==1.23.5 plotly==5.18.0