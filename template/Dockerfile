# =============================================================================
# FOM LaTeX Build Environment – Tectonic (Binary Install)
# =============================================================================
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates \
    libfontconfig1 libssl3 \
    libgraphite2-3 libharfbuzz0b libicu72 \
    fonts-texgyre fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Install Biber 2.17 (compatible with Tectonic's BibLaTeX 3.17)
RUN curl -L "https://sourceforge.net/projects/biblatex-biber/files/biblatex-biber/2.17/binaries/Linux/biber-linux_x86_64.tar.gz/download" -o biber.tar.gz \
    && tar -xzf biber.tar.gz \
    && chmod +x biber \
    && mv biber /usr/local/bin/ \
    && rm biber.tar.gz

# Install Tectonic binary directly
RUN curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh \
    && mv tectonic /usr/local/bin/

WORKDIR /data
VOLUME ["/data"]

ENTRYPOINT ["tectonic"]
CMD ["--help"]
